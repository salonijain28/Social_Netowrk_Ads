from flask import Flask, redirect, url_for, request,render_template
import pickle
import numpy as np
import sklearn
app = Flask(__name__)


def ValuePredictor(to_predict_list):
    X = np.array([to_predict_list]).reshape(1, 2)
    pkl = open('KMeansClusterpart3.pkl', 'rb')
    model1=pickle.load(pkl)
    result=model1.predict(X)
    return result



@app.route("/")
def index():
    return render_template("index.html");
@app.route('/result',  methods =['POST'])
def result():
    if request.method == "POST":
        to_predict_list = request.form.values()
        to_predict_list = list(map(int,to_predict_list))

        result=ValuePredictor(to_predict_list)
        print("result value:", result)
        if result == 0:
            prediction='Middle family:'

        elif result == 1:
            prediction='High family:'

        elif result == 2:
            prediction='Low family:'

        else:
            prediction='Invalid cluster input:'

    return render_template("result.html",prediction=prediction)


if __name__ == '__main__':
   app.run(debug = True)
