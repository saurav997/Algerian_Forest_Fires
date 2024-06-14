# from flask import Flask,request,jsonify,render_template
# import numpy as np
# import pickle
# import pandas as pd
# from sklearn.preprocessing import StandardScaler

# application = Flask(__name__)
# app = application

# LassoCV_model = pickle.load(open("Notebooks\Models\LassoCV_regression.pkl",'rb'))
# scaler = pickle.load(open("Notebooks\Models\standard_scaler.pkl",'rb'))

# @app.route("/")
# def homepage():
#     return render_template('index.html')

# @app.route('/predictdata',methods=['GET','POST'])
# def predict_data():
#     if request.method=='POST':
#         Temparature = float(request.form.get('Temparature'))
#         RH = float(request.form.get('RH'))
#         Ws = float(request.form.get('Ws'))
#         Rain = float(request.form.get('Rain'))
#         FFMC = float(request.form.get('FFMC'))
#         DMC = float(request.form.get('DMC'))
#         BUI = float(request.form.get('BUI'))
#         Classes = float(request.form.get('Classes'))
#         Region = float(request.form.get('Region'))
#         # ['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'BUI', 'Classes','Region']
#         new_datapoint = scaler.transform([[Temparature,RH,Ws,Rain,FFMC,DMC,BUI,Classes,Region]])
#         result = LassoCV_model.predict(new_datapoint)
#         return render_template('home.html',results = result[0])
#     else:
#         return render_template('home.html',results = None)


# if __name__ =="__main__":
#     app.run(host="0.0.0.0")

from flask import Flask, request, jsonify, render_template, send_from_directory
import numpy as np
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

LassoCV_model = pickle.load(open("Notebooks/Models/LassoCV_regression.pkl",'rb'))
scaler = pickle.load(open("Notebooks/Models/standard_scaler.pkl",'rb'))

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_data():
    if request.method=='POST':
        Temparature = float(request.form.get('Temparature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        BUI = float(request.form.get('BUI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))
        new_datapoint = scaler.transform([[Temparature, RH, Ws, Rain, FFMC, DMC, BUI, Classes, Region]])
        result = LassoCV_model.predict(new_datapoint)
        return render_template('home.html', results=result[0])
    else:
        return render_template('home.html', results=None)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ =="__main__":
    app.run(host="0.0.0.0")
