from flask import Flask, render_template, request, make_response
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from weasyprint import HTML

app = Flask(__name__)

# Load data
data = pd.read_csv(r'heart.csv')
X = data.drop(columns=['target'])
y = data['target']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
logistic_model = LogisticRegression(max_iter=1000)
logistic_model.fit(X_train, y_train)

# Feature importance chart
feature_names = X.columns
importance = logistic_model.coef_[0]
sorted_idx = np.argsort(np.abs(importance))[::-1]

plt.figure(figsize=(10, 6))
plt.bar(range(len(importance)), np.abs(importance[sorted_idx]), align='center', color='#ff7e5f')
plt.xticks(range(len(importance)), feature_names[sorted_idx], rotation=90)
plt.title("Feature Importance (Logistic Regression)")
plt.tight_layout()
plt.savefig("static/feature_importance.png")
plt.close()

# Global dictionary to store report data
report_data = {}

@app.route('/')
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        # Get input
        age = float(request.form.get('age', 0))
        sex = float(request.form.get('sex', 0))
        cp = float(request.form.get('cp', 0))
        trestbps = float(request.form.get('trestbps', 0))
        chol = float(request.form.get('chol', 0))
        fbs = float(request.form.get('fbs', 0))
        restecg = float(request.form.get('restecg', 0))
        thalach = float(request.form.get('thalach', 0))
        exang = float(request.form.get('exang', 0))
        oldpeak = float(request.form.get('oldpeak', 0))
        slope = float(request.form.get('slope', 0))
        ca = float(request.form.get('ca', 0))
        thal = float(request.form.get('thal', 0))

        # Prepare input array
        input_features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                                    thalach, exang, oldpeak, slope, ca, thal]])

        # Predict probability
        probability = logistic_model.predict_proba(input_features)[0][1]
        percent = round(probability * 100, 2)

        # Risk text
        if percent >= 70:
            risk_text = "High risk of heart disease."
        elif percent >= 40:
            risk_text = "Moderate risk of heart disease."
        else:
            risk_text = "Low risk of heart disease."

        # Suggestions
        suggestions = []
        if chol > 200:
            suggestions.append("Your cholesterol is high. Consider a low-fat diet, eat more vegetables, consult your doctor.")
        if trestbps > 120:
            suggestions.append("Your BP is high. Reduce salt, manage stress, consult doctor.")
        if age > 60:
            suggestions.append("Above 60 years. Regular heart screenings recommended.")
        if oldpeak > 2.0:
            suggestions.append("High ST depression. Manage stress, regular exercise advised.")
        if thalach < 120:
            suggestions.append("Low max heart rate. Check with doctor about heart fitness.")
        if not suggestions:
            suggestions.append("All parameters seem okay. Maintain your current healthy lifestyle.")

        # Store report data
        global report_data
        report_data = {
            "percent": percent,
            "risk_text": risk_text,
            "suggestions": suggestions
        }

        return render_template('result.html', 
                               percent=percent, 
                               risk_text=risk_text, 
                               suggestions=suggestions)

    except Exception as e:
        return f"<h3>Error: {e}</h3><a href='/'>Back</a>"

@app.route('/download_pdf')
def download_pdf():
    try:
        html_out = render_template('pdf_template.html', 
                                   percent=report_data["percent"], 
                                   risk_text=report_data["risk_text"], 
                                   suggestions=report_data["suggestions"])
        pdf = HTML(string=html_out).write_pdf()

        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=Heart_Report.pdf'
        return response
    except Exception as e:
        return f"<h3>Error in PDF generation: {e}</h3><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run(debug=True)
