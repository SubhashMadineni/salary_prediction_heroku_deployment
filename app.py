import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle                        #import the necessary bibraries


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))                   #loading the model which we saved using pickle

@app.route('/')
def home():
    return render_template('index.html')                   # opening the index .htm file where we stored the web page that is created using html

@app.route('/predict',methods=['POST'])                      #when submit button is pressed this function will execute and prints the prediction text as output. 
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)