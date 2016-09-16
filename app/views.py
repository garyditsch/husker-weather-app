import os
from flask import render_template, request
from flask import flash


from app import app
from app.forms import WeatherForm
from app.open_weather_api import OpenWeatherAPI

@app.route("/")
@app.route("/index")
def index():
    lincoln_weather_current = None
    bloomington_weather_current = None
    columbus_weather_current = None
    indianapolis_weather_current = None
    iowa_city_weather_current = None
    evanston_weather_current = None
    madison_weather_current = None

    api = OpenWeatherAPI(os.environ["OPEN_WEATHER_API_KEY"])
    lincoln_weather_current = api.get_lincoln_weather("lincoln")
    bloomington_weather_current = api.get_lincoln_weather("bloomington")
    columbus_weather_current = api.get_lincoln_weather("columbus")
    indianapolis_weather_current = api.get_lincoln_weather("indianapolis")
    iowa_city_weather_current = api.get_lincoln_weather("iowa_city")
    evanston_weather_current = api.get_lincoln_weather("evanston")
    madison_weather_current = api.get_lincoln_weather("madison")


    return render_template("index.html", lincoln_weather_current=lincoln_weather_current, 
        bloomington_weather_current=bloomington_weather_current, columbus_weather_current=columbus_weather_current,
        indianapolis_weather_current=indianapolis_weather_current,iowa_city_weather_current=iowa_city_weather_current, 
        evanston_weather_current=evanston_weather_current, madison_weather_current=madison_weather_current)

@app.route("/current", methods=["GET", "POST"])
def current_weather():
    weather_form = WeatherForm(request.form)
    weather_item = None

    if request.method == "POST" and weather_form.validate():
        #do stuff with the valid form
        city = weather_form.city.data
        country_code = weather_form.country_code.data

        try: 

            api = OpenWeatherAPI(os.environ['OPEN_WEATHER_API_KEY'], weather_form.units.data)
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

            api = OpenWeatherAPI(os.environ['OPEN_WEATHER_API_KEY'], weather_form.units.data)
            weather_list = api.get_daily_weather(city, country_code)
        except ValueError as e:
            flash(str(e), "warning")   

    return render_template("forecast.html", weather_form=weather_form, weather_list=weather_list)

@app.route("/lincoln")
def lincoln_weather_forecast():
    lincoln_forecast = None
    
    api = OpenWeatherAPI(os.environ['OPEN_WEATHER_API_KEY'])
    lincoln_forecast = api.get_lincoln_forecast('lincoln')
       
    return render_template("lincoln.html", lincoln_forecast=lincoln_forecast)

@app.route("/bloomington")
def bloomington_weather_forecast():
    lincoln_forecast = None
    
    api = OpenWeatherAPI(os.environ['OPEN_WEATHER_API_KEY'])
    lincoln_forecast = api.get_lincoln_forecast('bloomington')
       
    return render_template("bloomington.html", lincoln_forecast=lincoln_forecast)

@app.route("/columbus")
def columbus_weather_forecast():
    lincoln_forecast = None
    
    api = OpenWeatherAPI(os.environ['OPEN_WEATHER_API_KEY'])
    lincoln_forecast = api.get_lincoln_forecast('columbus')
       
    return render_template("columbus.html", lincoln_forecast=lincoln_forecast)

@app.route("/madison")
def madison_weather_forecast():
    lincoln_forecast = None
    
    api = OpenWeatherAPI(os.environ['OPEN_WEATHER_API_KEY'])
    lincoln_forecast = api.get_lincoln_forecast('madison')
       
    return render_template("madison.html", lincoln_forecast=lincoln_forecast)

@app.route("/evanston")
def evanston_weather_forecast():
    lincoln_forecast = None
    
    api = OpenWeatherAPI(os.environ['OPEN_WEATHER_API_KEY'])
    lincoln_forecast = api.get_lincoln_forecast('evanston')
       
    return render_template("evanston.html", lincoln_forecast=lincoln_forecast)

@app.route("/iowa-city")
def iowa_city_weather_forecast():
    lincoln_forecast = None
    
    api = OpenWeatherAPI(os.environ['OPEN_WEATHER_API_KEY'])
    lincoln_forecast = api.get_lincoln_forecast('iowa_city')
       
    return render_template("iowa-city.html", lincoln_forecast=lincoln_forecast)

@app.route("/indianapolis")
def indianapolis_weather_forecast():
    lincoln_forecast = None
    
    api = OpenWeatherAPI(os.environ['OPEN_WEATHER_API_KEY'])
    lincoln_forecast = api.get_lincoln_forecast('indianapolis')
       
    return render_template("indianapolis.html", lincoln_forecast=lincoln_forecast)

@app.route("/search", methods=["GET", "POST"])
def weather_search():
    weather_form = WeatherForm(request.form)
    weather_item = None
    weather_list = None

    if request.method == "POST" and weather_form.validate():
        #do stuff with the valid form
        city = weather_form.city.data
        country_code = weather_form.country_code.data

        try: 

            api = OpenWeatherAPI(os.environ['OPEN_WEATHER_API_KEY'], weather_form.units.data)
            weather_item = api.get_current_weather(city, country_code)
        except ValueError as e:
            flash(str(e), "warning")


    if request.method == "POST" and weather_form.validate():
        #do stuff with the valid form
        city = weather_form.city.data
        country_code = weather_form.country_code.data

        try: 

            api = OpenWeatherAPI(os.environ['OPEN_WEATHER_API_KEY'], weather_form.units.data)
            weather_list = api.get_daily_weather(city, country_code)
        except ValueError as e:
            flash(str(e), "warning")   

    return render_template("search.html", weather_form=weather_form, weather_list=weather_list, weather_item=weather_item)

