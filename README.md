
💖 Heart Disease Prediction Web Application
📄 Project Description
This project is an interactive and user-friendly web application that predicts a person’s risk of heart disease based on their health details. The application uses a Logistic Regression machine learning model, trained on the popular heart.csv dataset.

It collects input parameters (like age, cholesterol, blood pressure, etc.) from the user through a simple form, predicts the heart disease risk percentage, categorizes it into low, moderate, or high risk, and also provides personalized health suggestions.

🚀 Features
✅ Machine Learning Prediction — Predicts the risk of heart disease using Logistic Regression.
✅ User-Friendly Form — Collects user details easily and clearly.
✅ Risk Categorization — Displays risk as Low, Moderate, or High with a clear percentage.
✅ Personalized Suggestions — Provides advice based on entered values (e.g., high cholesterol warning).
✅ Feature Importance Chart — Shows which features most influence the prediction, helping users understand risk factors visually.
✅ Downloadable PDF Report — Users can download a personalized PDF report summarizing their results and suggestions.
✅ Attractive UI — Smooth animations and gradient backgrounds for an engaging user experience.

💻 How to Run This Project on Another System
Step 1: Clone or Copy the Project
Copy the entire project folder to the new system.

Make sure it contains:

sml.py (main Flask app)

Templates folder (templates/) with HTML files (predict.html, result.html, pdf_template.html)

Static folder (static/) with style.css and any images (e.g., feature importance plot).

Step 2: Install Python
Install Python (recommended version: 3.9 or higher).

Add Python to PATH during installation.

Step 3: Install Required Packages
Open a terminal (or command prompt) inside your project folder and run:

bash
Copy
Edit
pip install flask pandas numpy scikit-learn matplotlib weasyprint
If you face errors with WeasyPrint on Windows, follow official WeasyPrint Windows instructions.

Step 4: Place the Dataset
Make sure heart.csv is in the project folder.

If not already included, download from Kaggle Heart Disease Dataset.

Step 5: Run the App
In the terminal, run:

bash
Copy
Edit
python sml.py
You will see something like:

csharp
Copy
Edit
 * Running on http://127.0.0.1:5000
Open your browser and go to http://127.0.0.1:5000.

⚙️ How It Works
1️⃣ User enters health information (age, cholesterol, BP, etc.) on the home page.
2️⃣ The system predicts the risk percentage using the trained Logistic Regression model.
3️⃣ It shows:

Risk percentage and level (Low, Moderate, High).

Personalized suggestions and precautions.

Feature importance chart showing key health factors.
4️⃣ User can download a personalized PDF report summarizing the results.

⭐ Advantages
Helps create awareness about heart health.

Easy to use even for non-technical users.

Can be used as a preliminary tool before consulting a doctor.

Fully offline and runs locally on your system.

✅ Summary
This project combines data science, web development, and healthcare awareness into a single application that is practical, informative, and easy to use.
