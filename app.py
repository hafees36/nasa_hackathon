from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("kerala_climate_data.csv")
city_list = df['City'].tolist()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        city = request.form['city'].strip()
        if city in df['City'].values:
            row = df[df['City'] == city].iloc[0]
            rainfall = "Yes" if row['Rainfall'] == 1 else "No"
            preferred_location = "Indoor" if row['Rainfall'] == 1 else "Outdoor"
            
            result = {
                "City": row['City'],
                "Altitude": row['Altitude(m)'],
                "Temperature": row['Temperature(°C)'],
                "Humidity": row['Humidity(%)'],
                "WindSpeed": row['WindSpeed(km/h)'],
                "Rainfall": rainfall,
                "Preferred": preferred_location
            }
        else:
            result = {"error": "City not found in dataset."}

    return render_template('index.html', result=result, cities=city_list)

if __name__ == '__main__':
    app.run(debug=True)