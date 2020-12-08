from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from .forms import ExitedForm
from .serializers import exitedSerializers
from django.contrib import messages
import joblib
import json
import numpy as np
import pandas as pd
from sklearn import preprocessing
from collections import defaultdict, Counter
from . models import exited
#from keras import backened as K

class ExitedView(viewsets.ModelViewSet):
    queryset  =  exited.objects.all()
    serializer_class  =  exitedSerializers

def about(request):
    return render(request, 'myform/About.html')

def ohevalue(df):
    ohe_col = joblib.load("myAPI/ohe_col.joblib")
    cat_cols = ['Geography', 'Gender', 'Tenure', 'NumOfProducts']
    df_pro =  pd.get_dummies(df, columns = cat_cols)
    newdict = {}
    for i in ohe_col:
        if i in df_pro.columns:
            newdict[i] = df_pro[i].values
        else:
            newdict[i] = 0
    newdf =  pd.DataFrame(newdict)
    return newdf



#@api_view(["POST"])
def churn(unit):
    try:
        mdl = joblib.load("myAPI/churn_model.joblib")
        scaler = joblib.load("myAPI/scalar_churn_model.joblib")
        X = scaler.transform(unit)
        y_pred = mdl.predict(X)
        y_pred = (y_pred>0.5)
        newdf = pd.DataFrame(y_pred, columns =  ['Exited_or_not'])
        newdf = newdf.replace({True: 'Exits', False: 'Continues'})
        return ('{}'.format(newdf))
        '''
        K.clear_session()
        return(newdf.values[0][0],X[0])
        '''
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
        #return (e.args[0])


def cxcontact(request):
    sb=request.POST.get("submit")
    CreditScore=''
    Geography=''
    Gender=''
    Age=''
    Tenure=''
    Balance=''
    NumOfProducts=''
    HasCrCard=''
    hs=''
    IsActiveMember=''
    ia=''
    EstimatedSalary=''

    if request.method  == 'POST':
        form = ExitedForm(request.POST)
        if form.is_valid():
            CreditScore = form.cleaned_data['CreditScore']
            Geography = form.cleaned_data['Geography']
            Gender = form.cleaned_data['Gender']
            Age = form.cleaned_data['Age']
            Tenure = form.cleaned_data['Tenure']
            Balance = form.cleaned_data['Balance']
            NumOfProducts = form.cleaned_data['NumOfProducts']
            HasCrCard = form.cleaned_data['HasCrCard']
            IsActiveMember = form.cleaned_data['IsActiveMember']
            EstimatedSalary = form.cleaned_data['EstimatedSalary']
            my_dict = (request.POST).dict()
            df = pd.DataFrame(my_dict, index=[0])
            print(HasCrCard)
            if HasCrCard=='1':
                hs='Yes'
            else:
                hs='No'
            
            if IsActiveMember=='1':
                ia='Yes'
            else:
                ia='No'

            #df[['IsActiveMember', 'EstimatedSalary']] = df[['IsActiveMember', 'EstimatedSalary']].apply(pd.to_numeric)
            answer= churn(ohevalue(df)).split()[2]
            #answer= churn(ohevalue(df))[0]
            #Xscalars= churn(ohevalue(df))[1]
            
            if not(350<=(int(df['CreditScore']))<=850):
                messages.success(request, 'Invalid: Enter Credit Score with in limits')
            elif not(18<=(int(df['Age']))<=90):
                messages.success(request, 'Invalid: Enter Age with in limits')
            elif not(0<=(int(df['Balance']))<=250000):
                messages.success(request, 'Invalid: Enter Balance Amount with in limits')
            elif not(0<=(int(df['EstimatedSalary']))<=200000):
                messages.success(request, 'Invalid: Enter Estimated Salary with in limits')
            else :
                messages.success(request, 'Status: Member {}'.format(answer))
            
            
                
            

    form=ExitedForm()
    context = {'form': form,'CreditScore': CreditScore, 'Geography':Geography, 'Gender':Gender, 'Age':Age, 'Tenure':Tenure, 'Balance':Balance, 'NumOfProducts':NumOfProducts, 'HasCrCard':hs, 'IsActiveMember':ia, 'EstimatedSalary':EstimatedSalary, 'sb':sb}
    return render(request, 'myform/cxform.html', context)
