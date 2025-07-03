 Heart Disease Prediction Web Application
 
📄 Project Description
This project is a user-friendly web application that predicts an individual’s risk of heart disease based on their health details. The application uses a Logistic Regression machine learning model, trained on a heart disease dataset (heart.csv).

Users can input their health parameters, and the system predicts the risk percentage, categorizes the risk level (low, moderate, or high), provides health suggestions, shows a feature importance chart, and allows downloading a personalized PDF report.

🚀 Features

✅ Machine learning prediction using Logistic Regression.

✅ Interactive input form for user details.

✅ Risk percentage and level display (low, moderate, high).

✅ Personalized health suggestions.

✅ Feature importance visualization (bar chart).

✅ PDF report download option.

✅ Attractive UI with animations and gradients.

💻 How to Run This Project on Another 

Step 1: Copy the Project Files
Copy the entire project folder to the new system.

Ensure it contains:

sml.py (Flask main app)

templates/ folder with HTML files (predict.html, result.html, pdf_template.html)

static/ folder with style.css and feature_importance.png

heart.csv dataset.

Step 2: Install Python
Install Python (recommended version: 3.9 or above).

Check "Add Python to PATH" during installation.

Step 3: Install Required Python Packages
Open terminal (or command prompt) inside the project folder.

Run:

bash
Copy
Edit

pip install flask pandas numpy scikit-learn matplotlib weasyprint
Note: On Windows, WeasyPrint might require extra libraries. Check WeasyPrint installation guide if needed.

Step 4: Check Dataset
Ensure heart.csv is present in the project folder.

If missing, download it from Kaggle Heart Disease Dataset.

Step 5: Run the Flask Application
In terminal, run:

bash
Copy
Edit
python sml.py
You will see:

csharp
Copy
Edit
 * Running on http://127.0.0.1:5000
Open your browser and visit: http://127.0.0.1:5000.

⚙️ How It Works

1️⃣ User enters health details (e.g., age, cholesterol, BP, heart rate).

2️⃣ The model predicts the risk percentage of heart disease.

3️⃣ Displays risk level:

Low

Moderate

High

4️⃣ Provides personalized health suggestions.

5️⃣ Shows a feature importance chart to help understand key risk factors.

6️⃣ Option to download PDF report with prediction and suggestions.

⭐ Advantages

Raises awareness of heart health.

Easy and interactive for non-technical users.

Useful for initial health screening before consulting a doctor.

Fully offline, runs locally on your machine.

✅ Summary
This project integrates data science and healthcare in a simple web app that helps users understand their heart disease risk. It combines predictive analytics, visual insights, and health advice in a single, accessible platform.

