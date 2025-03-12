<h1>🌾 Crop Prediction & Fertilizer Recommendation App</h1>

A machine learning-based app that predicts crop types from images and provides the best fertilizer recommendations for optimal yield.

<h2>🚀 Features</h2>
	•	🌱 Crop Prediction: Upload a crop image, and the app will classify it using a deep learning model.
	•	🧪 Fertilizer Recommendation: Get specific fertilizer suggestions tailored to the identified crop.
	•	📊 Data-Driven Insights: Uses a well-structured dataset for fertilizer recommendations based on nutrient composition.
	•	💡 Simple & Fast: Built with Streamlit for a smooth and interactive UI.


<h2>⚙️ Installation</h2>

1️⃣ Clone the Repository

git clone https://github.com/Shivam007kumar/crop-fertilizer-app.git
cd crop-fertilizer-app

2️⃣ Set Up a Virtual Environment (Optional but Recommended)

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Download the Pre-Trained Model

📌 Download the CNN model from Kaggle:
🔗 https://www.kaggle.com/models/shivamkumar83/plant-prediction

📥 Steps to use the model:
	•	Download the crop_classification_cnn.h5 file from the link above.
	•	Place it in the project directory.

⸻

🏃‍♂️ Usage

1️⃣ Run the Application

streamlit run main.py

2️⃣ Upload a Crop Image
	•	Visit the Streamlit Web App in your browser.
	•	Upload a clear image of the crop.
	•	Get instant predictions of the crop name.

3️⃣ Get Fertilizer Recommendations
	•	Based on the predicted crop, the app suggests the best fertilizer (NPK ratio, application method, timing, etc.).
	•	Ensures data-driven, optimized farming solutions.

⸻

📂 Data

📌 The fertilizer recommendations are sourced from the fertilizer.csv file, which contains:
	•	Crop names (matching the model’s predictions).
	•	Recommended fertilizers based on nutrient composition.
	•	Application instructions for optimal crop growth.

⸻

🤝 Contributing

💡 Want to improve this project? Fork the repo, create a new branch, and submit a Pull Request with your updates!

⸻

📜 License

🔖 This project is MIT Licensed. See the LICENSE file for more details.

⸻

🙌 Acknowledgements

🚀 Special thanks to:
	•	The open-source community for datasets and resources.
	•	Kaggle for hosting the pre-trained model.
	•	Contributors who make this project better!

⸻

🔥 Start using the app today and optimize your farming with AI-powered insights! 🚀🌱
