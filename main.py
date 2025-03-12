import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array

# Load the trained CNN model
model = tf.keras.models.load_model("crop_classification_cnn.h5")

# Load fertilizer CSV
fertilizer_data = pd.read_csv("fertilizer.csv")

# Ensure class labels are correct
class_labels = {0: 'aloevera', 1: 'banana', 2: 'bilimbi', 3: 'cantaloupe', 4: 'cassava', 
                5: 'coconut', 6: 'corn', 7: 'cucumber', 8: 'curcuma', 9: 'eggplant', 
                10: 'galangal', 11: 'ginger', 12: 'guava', 13: 'kale', 14: 'longbeans', 
                15: 'mango', 16: 'melon', 17: 'orange', 18: 'paddy', 19: 'papaya', 
                20: 'pepper chili', 21: 'pineapple', 22: 'pomelo', 23: 'shallot', 
                24: 'soybeans', 25: 'spinach', 26: 'sweet potatoes', 27: 'tobacco', 
                28: 'waterapple', 29: 'watermelon'}

# Preprocessing function
def preprocess_image(img, target_size=(128, 128)):
    img = img.resize(target_size)  # Resize to model input size
    img = img.convert("RGB")  # Ensure it's in RGB format
    img = img_to_array(img)  # Convert to array
    img = np.expand_dims(img, axis=0)  # Expand for batch processing
    img /= 255.0  # Normalize
    return img

# Fertilizer recommendation function
def get_fertilizer_recommendation(predicted_crop):
    row = fertilizer_data[fertilizer_data['Plant Name'] == predicted_crop]
    if not row.empty:
        return {
            'Fertilizer Type': row.iloc[0]['Fertilizer Type(s)'],
            'NPK Ratio': row.iloc[0].get('NPK Ratio'),
            'Application Method': row.iloc[0].get('Application Method'),
            'Application Timing': row.iloc[0].get('Application Timing'),
            'Additional Notes': row.iloc[0].get('Additional Notes')
        }
    return None  # Return None when no recommendation is found

# Streamlit UI setup
st.set_page_config(page_title="Crop Predictor & Fertilizer Recommender", layout="centered")
st.title("🌱 Crop Prediction & Fertilizer Recommendation")
st.write("Upload an image of your crop, and we will predict its type and recommend a suitable fertilizer.")

# File uploader
uploaded_file = st.file_uploader("Upload Crop Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Process and predict
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    predicted_class = np.argmax(prediction, axis=1)[0]

    # Get predicted crop name
    predicted_crop = class_labels.get(predicted_class, "Unknown Crop")

    st.success(f"🌿 Predicted Crop: **{predicted_crop}**")

    # Get fertilizer recommendation
    recommendation = get_fertilizer_recommendation(predicted_crop)

    if recommendation:
        st.info(f"🛠️ Recommended Fertilizer: **{recommendation['Fertilizer Type']}**")
        st.write(f"📌 **NPK Ratio(s):** {recommendation['NPK Ratio']}")
        st.write(f"📌 **Application Method:** {recommendation['Application Method']}")
        st.write(f"📌 **Application Timing:** {recommendation['Application Timing']}")
        st.write(f"📌 **Additional Notes:** {recommendation['Additional Notes']}")
    else:
        st.warning("⚠️ No fertilizer recommendation found for this crop.")
