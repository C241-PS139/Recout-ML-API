from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
import requests
from sklearn.metrics.pairwise import cosine_similarity



app = Flask(__name__)

# Load OneHotEncoder and dataset
onehot_encoder = joblib.load('onehot_encoder.pkl')
ds = pd.read_csv('dataset.csv')

# Convert temperature to categories
def convert_temperature(temperature):
    if temperature < 20:
        return "Cold"
    elif 20 <= temperature < 30:
        return "Normal"
    else:
        return "Hot"

# Function to convert Kelvin to Celsius
def kelvin_to_celcius(kelvin):
    return kelvin - 273.15

# Recommendation function
def recommend_outfits(gender_product, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = '5b48d68ce066834a01e3b108a9e5891a'

    url = base_url + "appid=" + API_KEY + "&q=" + city
    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    temp_celcius = kelvin_to_celcius(temp_kelvin)
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celcius = kelvin_to_celcius(feels_like_kelvin)
    description = response['weather'][0]['description']

    temperature = convert_temperature(temp_celcius)

    features_onehot = onehot_encoder.transform(ds[['gender_product', 'temperature', 'city']])
    query_vector = onehot_encoder.transform(np.array([gender_product, temperature, city]).reshape(1, -1))
    similarities = cosine_similarity(query_vector, features_onehot)
    top_n = 5
    sorted_indices = similarities.argsort()[0][-top_n:]
    recommended_outfits = ds.iloc[sorted_indices]

    return recommended_outfits.to_dict('records')

@app.route('/recommend', methods=['POST'])
def get_recommendation():
    data = request.json
    gender_product = data.get('gender_product')
    city = data.get('city')
    recommendations = recommend_outfits(gender_product, city)
    return jsonify(recommendations)

@app.route('/hello', methods=['GET'])
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
