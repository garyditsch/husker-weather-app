from flask import render_template, request
from flask import flash

from app import app
from app.forms import WeatherForm
from app.open_weather_api import OpenWeatherAPI

@app.route("/")
@app.route("/index")
def index():
    lincoln_weather_current = None

    api = OpenWeatherAPI(app.config["OPEN_WEATHER_API_KEY"])
    lincoln_weather_current = api.get_lincoln_weather()

    return render_template("index.html", lincoln_weather_current=lincoln_weather_current)

@app.route("/current", methods=["GET", "POST"])
def current_weather():
    weather_form = WeatherForm(request.form)
    weather_item = None

    if request.method == "POST" and weather_form.validate():
        #do stuff with the valid form
        city = weather_form.city.data
        country_code = weather_form.country_code.data

        try: 

            api = OpenWeatherAPI(app.config["OPEN_WEATHER_API_KEY"], weather_form.units.data)
            weather_item = api.get_current_weather(city, country_code)
        except ValueError as e:
            flash(str(e), "warning")

    print(weather_item)


    return render_template("current.html", 
        weather_form=weather_form, weather_item=weather_item)

@app.route("/forecast", methods=["GET", "POST"])
def forecast_weather():
    weather_form = WeatherForm(request.form)
    weather_list = None

    if request.method == "POST" and weather_form.validate():
        #do stuff with the valid form
        city = weather_form.city.data
        country_code = weather_form.country_code.data

        try: 

            api = OpenWeatherAPI(app.config["OPEN_WEATHER_API_KEY"], weather_form.units.data)
            weather_list = api.get_daily_weather(city, country_code)
        except ValueError as e:
            flash(str(e), "warning")   

    return render_template("forecast.html", weather_form=weather_form, weather_list=weather_list)

@app.route("/lincoln")
def lincoln_weather_forecast():
    lincoln_forecast = None
    
    api = OpenWeatherAPI(app.config["OPEN_WEATHER_API_KEY"])
    lincoln_forecast = api.get_lincoln_forecast()
       
    return render_template("lincoln.html", lincoln_forecast=lincoln_forecast)
