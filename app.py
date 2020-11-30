from flask import Flask, render_template, url_for, flash, redirect
import joblib
from flask import request
import numpy as np


app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/disclimer")
def disclimer():
    return render_template("disclimer.html")

# cancer
@app.route("/Breast_CancerAPI")
def cancer():
    return render_template("cancer.html")

def ValuePredictor1(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==5):
        loaded_model = joblib.load('cancer_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]


#Cancer
@app.route('/predict1', methods = ["POST"])
def predict1():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         
        if(len(to_predict_list)==5):
            result = ValuePredictor1(to_predict_list,5)
    
    if(int(result)==1):
        prediction = "Tienes, probablemente, altas las posibilidades.                 Por favor, consulte a su médico."
    else:
        prediction = "No debes de preocuparte.                     No obstante, en caso de duda, te recomiendo que realices una consulta a tu médico."
    return(render_template("result.html", prediction_text=prediction))  








# diabetes 
@app.route("/Diabetes_API")
def diabetes():
    return render_template("diabetes.html")

def ValuePredictor2(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==6):
        loaded_model = joblib.load('diabetes_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

#diabetes
@app.route('/predict2', methods = ["POST"])
def predict2():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #diabetes
        if(len(to_predict_list)==6):
            result = ValuePredictor2(to_predict_list,6)
    
    if(int(result)==1):
        prediction = "Tienes, probablemente, altas las posibilidades.                 Por favor, consulte a su médico."
    else:
        prediction = "No debes de preocuparte.                     No obstante, en caso de duda, te recomiendo que realices una consulta a tu médico."
    return(render_template("result.html", prediction_text=prediction))     




#heart   
@app.route("/Heart_API")
def heart():
    return render_template("heart.html")

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load('heart_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]   


# heart    
@app.route('/predict3', methods = ["POST"])
def predict3():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #heart
        if(len(to_predict_list)==7):
            result = ValuePredictor(to_predict_list,7)
    
    if(int(result)==1):
        prediction = "Creo que tienes altas las posibilidades de contraer la enfermedad.                 Por favor, consulte a su médico inmediatamente"
    else:
        prediction = "No hay necesidad de temer.            No tienes síntomas peligrosos de la enfermedad.                No obstante te recomiendo que realices una consulta a tu médico."
    return(render_template("result.html", prediction_text=prediction))   
    







    
#kidney
@app.route("/Kidney_API")
def kidney():
    return render_template("kidney.html")

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load('kidney_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]


    

# Kidney
@app.route('/predict4', methods = ["POST"])
def predict4():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #Kidney
        if(len(to_predict_list)==7):
            result = ValuePredictor(to_predict_list,7)
    
    if(int(result)==1):
        prediction = "Creo que tienes altas las posibilidades de contraer la enfermedad.                 Por favor, consulte a su médico inmediatamente"
    else:
        prediction = "No hay necesidad de temer.            No tienes síntomas peligrosos de la enfermedad.                No obstante te recomiendo que realices una consulta a tu médico."
    return(render_template("result.html", prediction_text=prediction))    








# liver
@app.route("/Liver_API")
def liver():
    return render_template("liver.html")

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load('liver_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]




@app.route('/predict5', methods = ["POST"])
def predict5():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         
        if(len(to_predict_list)==7):
            result = ValuePredictor(to_predict_list,7)
    
    if(int(result)==1):
        prediction = "Creo que tienes altas las posibilidades de contraer la enfermedad.  \n  Por favor, consulte a su médico inmediatamente"
    else:
        prediction = "No hay necesidad de temer.   ,'\n'   No tienes síntomas peligrosos de la enfermedad.  '\n'  No obstante te recomiendo que realices una consulta a tu médico."
    return(render_template("result.html", prediction_text=prediction))  


   




