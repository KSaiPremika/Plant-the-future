from flask import Flask, request, render_template

import pandas as pd
import pyrebase
import numpy as np
import os
import shutil
from test import *

config ={
"apiKey": "AIzaSyDgVVBiPybGnCYHodfO4hySSXiVgUltJmI",
    "authDomain": "test-7ecc9.firebaseapp.com",
    "databaseURL": "https://test-7ecc9.firebaseio.com",
    "projectId": "test-7ecc9",
    "storageBucket": "test-7ecc9.appspot.com",
    "messagingSenderId": "77865940073",
    "appId": "1:77865940073:web:3bf93963e7ed8d9f729ef8",
    "measurementId": "G-FTN63R6BXP"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

app = Flask(__name__)

indexGlobal = 0;

@app.route('/')
def home():
    addressesForAutocomplete = np.array(df_address.loc[df_address['Completed'] == True]['Address']).tolist()

    return render_template('home.html',addresses=addressesForAutocomplete)

@app.route('/learn')
def learn():


    return render_template('learn.html')


@app.route('/vote')
def vote():


    return render_template('vote.html')



@app.route('/images',methods=['GET','POST'])
def images():
    global indexGlobal

    print("indexGlobal in images()",indexGlobal)

    treesAndArea = copyToDes(indexGlobal)
    imagesNames = getPlottedImages(indexGlobal)


    for section, img in zip(treesAndArea,imagesNames):
        section['imageName'] = 'images/'+str(indexGlobal)+'/'+img



    return render_template('images.html',treesAndArea=treesAndArea)


@app.route('/sign_in',methods=['GET','POST'])
def sign_in():
    unsuccessful = 'You have not signed up with us !!'
    successful = 'Login successful'



    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template('sign_in.html', s=successful)
        except Exception:
            return render_template('sign_in.html', us=unsuccessful)

    return render_template('sign_in.html')

@app.route('/graph',methods=['GET'])
def graph():
    global indexGlobal
    index = 0


    if request.method == 'GET' and request.args:
        #index = str(request.args.get('area'))
        #print("Index :",index)
        index = df_address.loc[df_address['Address'] == str(request.args.get('area'))].index[0]
        print(index)

    else:
        index = 1
    
    address_row = df_address.iloc[index,:]
    indexGlobal = index
    print("indexGlobsl",indexGlobal)

    address_row = dict({'Address':address_row['Address'],
                        'Street':address_row['Street'],
                        'Location':address_row['Location'],
                        'Traffic Threshold':address_row['Traffic Threshold'].astype(str),
                        'Construction Year':address_row['Construction Year'].astype(str)})
    
    

    values_train = list(df_traffic.iloc[:,index+1].astype(int))
    labels_train = list(df_traffic['day_stamp'])


    data_plot = []
    for x,y in zip(labels_train,values_train):
        data_plot.append(dict({'x':x,'y':y}))

    dataset_train = dict({'data_plot':data_plot,'label_plot':labels_train})

    values_pred = list(df_traffic_predict.iloc[:, index+1].astype(int))
    labels_pred = list(df_traffic_predict['day_stamp'])

    data_pred = []
    for x, y in zip(labels_pred, values_pred):
        data_pred.append(dict({'x': x, 'y': y}))

    dataset_pred = dict({'data_plot': data_pred, 'label_plot': labels_pred})



    dataset = dict({'address':address_row,'dataset_train':dataset_train,'dataset_pred':dataset_pred})



    return render_template('graph.html',data_to_plot=dataset)







df_address = pd.read_csv('datasets/Addresses_with_threshold_and_year.csv')
df_traffic = pd.read_csv('datasets/Traffic_density_day_by_day_2000_to_2019.csv')
df_traffic_predict = pd.read_csv('datasets/Traffic_density_day_by_day_2020_to_2025.csv')



app.run(debug=True)