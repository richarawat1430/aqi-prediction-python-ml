import pickle
from flask import Flask, render_template, request

# Load trained model
model = pickle.load(open("aqi_model.pkl", "rb"))
print("MODEL TYPE:", type(model), flush=True)

app = Flask(__name__)

# AQI Category Logic
def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good", "#00b894", "Air quality is satisfactory, and air pollution poses little or no risk. Enjoy your day! 😊"
    elif aqi <= 100:
        return "Moderate", "#f1c40f", "Air quality is acceptable. However, sensitive individuals should avoid prolonged outdoor exertion. 🙂"
    elif aqi <= 200:
        return "Poor", "#e67e22", "Health effects may be experienced by everyone. Members of sensitive groups may experience more serious effects. ⚠️"
    else:
        return "Severe", "#e74c3c", "Health warnings of emergency conditions. The entire population is more likely to be affected. 🚫"
    
# 🚨 Alert System Logic
def get_alert(aqi):
    if aqi > 200:
        return "🚨 Severe Alert! Avoid going outside. Wear a mask and stay indoors.", "severe"
    elif aqi > 100:
        return "⚠️ Warning! Limit outdoor activities and reduce exposure.", "warning"
    elif aqi > 50:
        return "🙂 Moderate air quality. Sensitive people should take care.", "moderate"
    else:
        return "✅ Air is safe. Enjoy your day!", "good"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/guide")
def guide():
    return render_template("guide.html")

@app.route("/live-aqi")
def live_aqi():
    return render_template("live_aqi.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            # Get data from form
            city = request.form.get("city")
            temp = float(request.form["temp"])
            humidity = float(request.form["humidity"])
            prev_aqi = float(request.form["prev_aqi"])

            # ML Prediction
            input_data = [[temp, humidity, prev_aqi]]
            predicted_aqi = int(model.predict(input_data)[0])

            # ✅ FIX: handle negative values
            aqi = max(0, predicted_aqi)

            # ✅ Color + category logic
            if aqi <= 50:
                color = "#2ecc71"
                category = "Good"
            elif aqi <= 100:
                color = "#f1c40f"
                category = "Moderate"
            elif aqi <= 200:
                color = "#e67e22"
                category = "Unhealthy"
            else:
                color = "#e74c3c"
                category = "Hazardous"

            # Suggestions + Alerts (use fixed AQI)
            suggestion = get_aqi_category(aqi)[2]
            alert, alert_type = get_alert(aqi)

            return render_template(
                "predict.html",
                result=aqi,   # ✅ use fixed value
                category=category,
                color=color,
                city=city,
                suggestion=suggestion,
                alert=alert,
                alert_type=alert_type
            )

        except Exception as e:
            return f"Error: Please enter valid values. {e}"

    return render_template("predict.html")
if __name__ == "__main__":
    app.run(debug=True, port=5000)