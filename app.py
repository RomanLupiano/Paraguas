from flask import Flask, render_template, request
import requests

API_KEY = '1350767293eef6c07127ff209dd93d7a'

app = Flask('__name__')

def get_weather_data(city_name):
    return 

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        city = request.form.get('Malaga')
        data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')

        json_object = data.json()

        temp = float(json_object['main']['temp'])
        return render_template('home.html', temperature=temp)
    else:
        return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__== '__main__':
    app.run(debug=True)