from django.shortcuts import render
import pandas as pd
#from sklearn.externals import joblib
#import sklearn.external.joblib as extjoblib
#import joblib
import numpy as np
from joblib import dump, load
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'home.html' )

def home(request):
    if request.method == 'GET':
        CRIM = float(request.GET['CRIME'])
        ZN = float(request.GET['ZN'])
            #INDUS = float(request.POST['INDUS'])
        #CHAS = float(request.GET['CHAS'])
            #NOX = float(request.POST['NOX'])
        RM = float(request.GET['RM'])
            #AGE = float(request.POST['AGE'])
            #DIS = float(request.POST['DIS'])
            #RAD = float(request.POST['RAD'])
        TAX = float(request.GET['TAX'])
            #PTRATIO = float(request.POST['PTRATIO'])
            #B = float(request.POST['B'])
        LSTAT = float(request.GET['LSTAT'])
        TAXRM = float(request.GET['TAXRM'])
        pred_args = [ RM, LSTAT, CRIM, ZN, TAX, TAXRM ]
           	
        pred_args_arr = np.array([pred_args])
        mul_reg = open("./ran_modell.joblib", "rb")
        model = load(mul_reg)
        model_prediction =model.predict(pred_args_arr)
        model_prediction = round(float(model_prediction), 2)
        context ={ 'mango': model_prediction }
    return render(request, 'predict.html' , context )