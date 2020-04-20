#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 20:43:58 2018

@author: abhilashsk
"""

import pandas as pd
import pymongo
from pymongo import MongoClient
import numpy as np

def read_data():
    data=pd.read_csv('train.csv')
    return data

def store_data(df_train):
    print("Storing data")
    client=MongoClient('localhost',27017)
    collection=client.test.HousePrice
    collection.remove({})
    del df_train['Id']
    cols=df_train.columns
    shape=df_train.shape
    print(shape)
    x=np.int64(1)
    try:
        for i in range(shape[0]):
            post={}
            post['_id']=i
            if i in [1379]:
                continue
            for j in cols:
                if type(df_train[j][i])==type(x):
                    post[j]=int(df_train[j][i])
                else:
                    post[j]=df_train[j][i]
            collection.insert(post)
    except KeyError:
        print("Error occurred")
    print("Storing data : Success")

def clean_data(df_train):
    print("Data cleaning")
    #missing data
    total = df_train.isnull().sum().sort_values(ascending=False)
    percent = (df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])

    #dealing with missing data
    df_train = df_train.drop((missing_data[missing_data['Total'] > 1]).index,1)
    df_train = df_train.drop(df_train.loc[df_train['Electrical'].isnull()].index)

    print("Data cleaning : Success")
    return df_train

def read_from_mongo():
    print("Reading data from HousePrice collection in mongodb")
    client=MongoClient('localhost',27017)
    collection=client.test.HousePrice
    x=collection.find()
    df=pd.DataFrame(columns=list(x[0].keys()))
    for i,item in enumerate(x):
        df.loc[i]=list(item.values())
    for col in df.columns:
        if type(df[col][0])==type(0):
            pd.to_numeric(df[col])
    print("Reading data from mongo : Success")
    return df





#data=read_data()
#data=clean_data(data)
#store_data(data)
#data=read_from_mongo()
