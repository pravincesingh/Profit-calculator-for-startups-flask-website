from flask import Flask, render_template ,request
from sklearn.externals import joblib
import pandas as pd
import numpy as np

app =Flask(__name__)

mul_reg =oepn("multiple_linear_regression.pkl","rb")
ml_model = joblib.load(mul_reg)

@app.route('/')
def home():
    return render_template('first.html')

@app.route("/predict",method =['GET','POST'])
def predict():
    if request.method =="POST":
        try:
            NewYork = float(request.form['NewYork'])
            California =float(request.form['California'])
            Florida = float(request.form['Florida'])
            RnDSpend =request.form['RnDSpend']
            AdminSpend = request.form['AdminSpend']
            MarketSpend= request.form['MarketSpend']
            pred_args = [NewYork,California,Florida,RnDSpend,AdminSpend,MarketSpend]
            pred_args_arr=np.array(pred_args)
            pred_args_arr=pred_args_arr.reshape(1,-1)
            # mul_reg =oepn("multiple_linear_regression.pkl","rb")
            # ml_model = joblib.load(mul_reg)
            model_prediction = ml_model.predict(pred_args_arr)
            model_prediction= round(flaot(model_prediction),2)

        exception ValueError:
            return "Please check if the value are entered correctly"

    return rander_template('predict.html',prediction= mdoel_prediction )

if __name__ == "__main__":
    app.run()