from flask import Flask,request,jsonify,render_template
import numpy as np
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
application = Flask(__name__)
app = application

LassoCV_model = pickle.load(open("Notebooks\Models\LassoCV_regression.pkl",'rb'))
scaler = pickle.load(open("Notebooks\Models\standard_scaler.pkl",'rb'))

@app.route("/")
def homepage():
    return render_template('index.html')

if __name__ =="__main__":
    app.run(host="0.0.0.0")