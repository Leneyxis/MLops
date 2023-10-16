import pandas as pd
import numpy as np
import matplotlib.pyplot as mat
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from flask import Flask, render_template, request


app = Flask(__name__)
cols = ['R&D Spend', 'Administration', 'Marketing Spend']

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/predict',methods=['POST'])
def predict():
    dataset=pd.read_csv('50_Startups.csv')
    X=dataset.iloc[:,:-2].values
    y=dataset.iloc[:,-1].values
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)
    regressor=LinearRegression()
    regressor.fit(X_train,y_train)
    int_features = [x for x in request.form.values()]
    final = np.array(int_features,dtype=np.float64)
    final = final.reshape(1,-1)
    prediction = regressor.predict(final)
    result=round(prediction[0],2)
    return render_template('home.html',pred='Expected profit for the startup will be {}'.format(result))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)