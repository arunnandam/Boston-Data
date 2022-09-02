#Flask Application

#Importing the packages
import pickle
from flask import Flask, request, app, jsonify, render_template, url_for
import numpy as np
import pandas as pd


#Starting point of the application
app = Flask(__name__)

#Loading pickle files - model and standard scaler
model = pickle.load(open('boston.pkl','rb'))
scaler = pickle.load(open('scaling.pkl','rb'))

@app.route('/')
#redirecting to the home page
def home():
    return render_template('home.html')

#function to test the flask application
@app.route('/test',methods=['POST'])
def test():
    print("flask test")
    data = request.json['data']
    print(data)
    return data

@app.route('/predict_api', methods=['POST'])
#creating an api to send request and get the predictions
def predict_api():
    print('arun')
    data = request.json["data"]
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    transformed_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    print(transformed_data)
    output = model.predict(transformed_data)
    print(output[0])
    return jsonify(output[0])


@app.route("/predict",methods=['POST'])
#creating prediction api when the input is passed over html form and recieve a prediction in that page itself
def predict():
    data = [float(x) for x in request.form.values()]
    transformed_data = scaler.transform(np.array(data).reshape(1,-1))
    print(transformed_data)
    output = model.predict(transformed_data)[0]
    return render_template('home.html', prediction_text = "The house price for the {}".format(output))

    
if __name__=="__main__":
    app.run(debug=True)
