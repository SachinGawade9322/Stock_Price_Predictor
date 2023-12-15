from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

app = Flask(__name__)

# Load your model and scaler
model = joblib.load(open(r'C:\Users\Admin\OneDrive\Desktop\Coca_cola_project\models\predictionModel.pkl', 'rb'))
standard_scaler = joblib.load(open(r'C:\Users\Admin\OneDrive\Desktop\Coca_cola_project\models\StandardScaler.pkl', 'rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictform', methods=['GET', 'POST'])
def predict_form():
    def predict_form():
        if request.method == 'POST':
            open_price = float(request.form.get('open'))
            high_price_str = request.form.get('high')
            high_price = float(high_price_str) if high_price_str is not None else 0.0  # Convert to float only if not None
            low_price = float(request.form.get('low'))
            volume = float(request.form.get('volume'))
            day = float(request.form.get('day'))
            month = float(request.form.get('month'))
            year = float(request.form.get('year'))

        new_data = [[open_price, high_price, low_price, volume, day, month, year]]
        prediction = model.predict(new_data)[0]
        print(prediction)

        return render_template('result.html', prediction=prediction)

    return render_template('predictform.html')

if __name__ == "__main__":
    app.run(debug=True)
