
# 🌍Smart AQI Predictor using AI and Data Analysis

An AI-based system that analyzes past air quality and weather data to forecast future AQI and alert users in advance.


# Project overview
This project focuses on developing a smart system that uses historical air quality and weather data to predict future AQI levels. It helps users understand pollution trends and prepares them in advance through early warnings and insights.

# Features
## 🌍 Prediction Engine
- Predicts AQI using historical data  
- Uses temperature, humidity, and previous AQI  
- Classifies air quality (Good, Moderate, Unhealthy, Hazardous)  

## 📊 Data Processing
- Data cleaning and preprocessing  
- Feature selection for better accuracy  
- Handles missing values  

## 🤖 AI Models Used
- Linear Regression  
- Decision Tree  

## 🎛️ User Interface
- Simple and interactive web app  
- User input-based prediction  
- Color-based AQI visualization  

## 🚨 Health Alerts
- AQI-based health suggestions  
- Alerts for unsafe air conditions  


# Tech Stack

- HTML, CSS, JavaScript  
- Python (Flask)  
- Scikit-learn  
- NumPy, Pandas 


# Installation

```md
Follow these steps to run the project locally:

# Clone repository
Clone the repository
```bash
git clone https://github.com/richarawat1430/aqi-prediction-python-ml.git
cd aqi-prediction-python-ml

# Backend setup
cd website/Backend
pip install -r requirements.txt
npm install

# Frontend setup
cd ../Frontend
npm install
```

# 📊 Dataset Overview

The dataset includes air pollution and weather parameters such as PM2.5, PM10, temperature, humidity, and AQI.

![Dataset Sample](https://github.com/richarawat1430/aqi-prediction-python-ml/blob/master/Picture1.png?raw=true)
# Example Response

{
  "city": "Ahmedabad",
  "temperature": 30,
  "humidity": 65,
  "previous_aqi": 120,
  "predicted_aqi": 145,
  "category": "Unhealthy",
  "health_advice": "Limit outdoor activities and wear a mask if necessary"
}
# Documentation

### 📁 Project Structure

AQI-Prediction-System/
├── static/               # CSS, JS, images  
├── templates/            # HTML files (Flask)  
├── model/                # Trained ML model file  
├── app.py                # Main Flask application  
├── requirements.txt      # Project dependencies  
└── README.md             # Project documentation

# Acknowledgements

 - [AI for SDGs Observatory](https://ai-for-sdgs.academy/observatory#7%20Affordable%20and%20Clean%20Energy)
 


# 🔗 Links
- GitHub: https://github.com/richarawat1430
- LinkedIn: https://www.linkedin.com/in/richarrawat/


