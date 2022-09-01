from flask import Flask, render_template, request
import requests
import configparser

app = Flask('__name__')

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form.get('city')

        if city == '':
            return render_template('home.html')

        data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={get_api_key()}&units=metric').json()

        return render_template('home.html', 
        temperature=data['main']['temp'],
        feels_like=data['main']['feels_like'],
        pressure=data['main']['pressure'],
        humidity=data['main']['humidity'],
        Feels_like=data['main']['humidity'])
    else:
        return render_template('home.html', data='')

@app.route('/find-city/<lat>/<lon>/')
def get_url_data(lat, lon):
    data = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={get_api_key()}&units=metric').json()
    temperature = data['current']['temp']
    if temperature < 20:
        answer1 = 'yes'
        answer2 = 'yes'

    
    return render_template('home.html', 
        temperature=temperature,
        feels_like=data['current']['feels_like'],
        pressure=data['current']['pressure'],
        humidity=data['current']['humidity'],
        clouds=data['current']['clouds'],
        wind_speed=data['current']['wind_speed'],
        hourly_pop=data['hourly'][0]['pop'],
        daily_pop=data['daily'][0]['pop'],
        answer1=answer1,
        answer2=answer2)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__== '__main__':
    app.run(debug=True)