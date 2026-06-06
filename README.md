# 🌦 Weather SaaS Dashboard (Django)

A modern SaaS-style weather application built with **Django + Weather AI API**, deployed on Render.

It provides real-time weather data and 7-day forecasts through a clean dashboard UI.

---

## 🚀 Live Demo

👉 https://weather-test-k2sv.onrender.com/

---

## 📸 Features

- 🌡 Real-time weather data
- 📊 7-day weather forecast
- 💧 Humidity tracking
- 🌬 Wind speed display
- ☁ Weather condition summary
- 🌍 Latitude/Longitude input support
- 🎨 SaaS-style UI dashboard
- ☁ Deployed on Render

---

## 🏗 Tech Stack

- Backend: Django 6
- Frontend: HTML, CSS, JavaScript
- API: Weather AI API
- Deployment: Render
- Environment Management: python-dotenv

---

## 📦 Project Structure

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/vinnyotach7/Weather-App
cd weather-saas

### 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Create .env file
SECRET_KEY=your_django_secret_key
WEATHER_AI_API_KEY=your_weather_api_key

### 5. Run migrations
python manage.py migrate

### 6. Start Server
python manage.py runserver

🌐 API Endpoints
 ### Current Weather
 GET /api/weather/?lat=-1.2921&lon=36.8219&days=1
 ### Forecast Weather
 GET /api/weather/?lat=-1.2921&lon=36.8219&days=7

 🚀 Deployment (Render)
 1.Push to Github
 2.Connect repo to Render
 3.Add environment variables: Secret_Key and WEATHER_AI_API_KEY
 4.Build Command:
  ## pip install -r requirements.txt
 5.Start Command:
  ## gunicorn farmer_weather.wsgi:application

📌 Future Improvements
 1.User authentication (login/signup)
 2.Saved locations per user
 3.Weather charts (Chart.js)
 4.Mobile app version
 5.Subscription-based SaaS model

 👨‍💻 Author

Built as a SaaS learning project using Django and Weather AI API.

---

# 🚀 WHY THIS README IS “PRO LEVEL”

This version shows:
✔ Clear architecture  
✔ Setup instructions (devs can run it easily)  
✔ API documentation  
✔ Deployment steps  
✔ SaaS roadmap  

This is exactly what reviewers want.

---

# 📦 NEXT STEP (IMPORTANT)

After updating README:

```bash
git add README.md
git commit -m "Improve README with production setup instructions"
git push origin main