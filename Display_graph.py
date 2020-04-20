#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 22:44:33 2018

@author: abhilashsk
"""
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import pandas as pd
import numpy as np


def displayGraph(type_graph,data):
    if type_graph.get():
        type_graph=type_graph.get()
        print(type_graph)
    else:
        print("No button selected")
        
    if type_graph=='1':
        var = 'GrLivArea'
        data = pd.concat([data['SalePrice'], data[var]], axis=1)
        data.plot.scatter(x=var, y='SalePrice', ylim=(0,800000));
    elif type_graph=='2':
        #scatter plot totalbsmtsf/saleprice
        var = 'TotalBsmtSF'
        data = pd.concat([data['SalePrice'], data[var]], axis=1)
        data.plot.scatter(x=var, y='SalePrice', ylim=(0,800000));
    elif type_graph=='3':
        #box plot overallqual/saleprice
        var = 'OverallQual'
        data = pd.concat([data['SalePrice'], data[var]], axis=1)
        f, ax = plt.subplots(figsize=(8, 6))
        fig = sns.boxplot(x=var, y="SalePrice", data=data)
        fig.axis(ymin=0, ymax=800000);
    elif type_graph=='4':
        var = 'YearBuilt'
        data = pd.concat([data['SalePrice'], data[var]], axis=1)
        f, ax = plt.subplots(figsize=(16, 8))
        fig = sns.boxplot(x=var, y="SalePrice", data=data)
        fig.axis(ymin=0, ymax=800000);
        plt.xticks(rotation=90);
    elif type_graph=='5':
        #correlation matrix
        corrmat = data.corr()
        f, ax = plt.subplots(figsize=(12, 9))
        sns.heatmap(corrmat, vmax=.8, square=True);
    elif type_graph=='6':
        #saleprice correlation matrix
        corrmat = data.corr()
        k = 10 #number of variables for heatmap
        cols = corrmat.nlargest(k, 'SalePrice')['SalePrice'].index
        cm = np.corrcoef(data[cols].values.T)
        sns.set(font_scale=1.25)
        hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', 
                         annot_kws={'size': 10}, yticklabels=cols.values, 
                         xticklabels=cols.values)
    elif type_graph=='7':
        #scatterplot
        sns.set()
        cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
        sns.pairplot(data[cols], size = 2.5)
    elif type_graph=='8':
        #histogram and normal probability plot
        sns.distplot(data['SalePrice'],fit=norm);
        fig = plt.figure()
        res = stats.probplot(data['SalePrice'], plot=plt)
    elif type_graph=='9':
        #applying log transformation
        data['SalePrice'] = np.log(data['SalePrice'])
        #transformed histogram and normal probability plot
        sns.distplot(data['SalePrice'], fit=norm);
        fig = plt.figure()
        res = stats.probplot(data['SalePrice'], plot=plt)
    elif type_graph=='10':
        #histogram and normal probability plot
        sns.distplot(data['GrLivArea'], fit=norm);
        fig = plt.figure()
        res = stats.probplot(data['GrLivArea'], plot=plt)
    elif type_graph=='11':
        #data transformation
        data['GrLivArea'] = np.log(data['GrLivArea'])
        #transformed histogram and normal probability plot
        sns.distplot(data['GrLivArea'], fit=norm);
        fig = plt.figure()
        res = stats.probplot(data['GrLivArea'], plot=plt)
    elif type_graph=='12':
        #histogram and normal probability plot
        sns.distplot(data['TotalBsmtSF'], fit=norm);
        fig = plt.figure()
        res = stats.probplot(data['TotalBsmtSF'], plot=plt)
    elif type_graph=='13':
        #create column for new variable (one is enough because it's a binary categorical feature)
        #if area>0 it gets 1, for area==0 it gets 0
        data['HasBsmt'] = pd.Series(len(data['TotalBsmtSF']), index=data.index)
        data['HasBsmt'] = 0 
        data.loc[data['TotalBsmtSF']>0,'HasBsmt'] = 1
        #transform data
        data.loc[data['HasBsmt']==1,'TotalBsmtSF'] = np.log(data['TotalBsmtSF'])
        #histogram and normal probability plot
        sns.distplot(data[data['TotalBsmtSF']>0]['TotalBsmtSF'], fit=norm);
        fig = plt.figure()
        res = stats.probplot(data[data['TotalBsmtSF']>0]['TotalBsmtSF'], plot=plt)

    plt.show()

def getDescription(type_graph):
    if type_graph.get():
        type_graph=type_graph.get()
        print(type_graph)
    else:
        print("No button selected")
        
    if type_graph=='1':
        return "The two values with bigger 'GrLivArea' seem strange and they are not following the crowd."
    elif type_graph=='2':
        return "TotalBsmtSF is correlated with SalePrice"
    elif type_graph=='3':
        return "OverallQual is correlated with SalePrice"
    elif type_graph=='4':
        return "YearBuilt is correlated with SalePrice"
    elif type_graph=='5':
        return "At first sight, there are two red colored squares that get my attention. The first one refers to the 'TotalBsmtSF' and '1stFlrSF' variables, and the second one refers to the 'GarageX' variables. Both cases show how significant the correlation is between these variables. Actually, this correlation is so strong that it can indicate a situation of multicollinearity. "
    elif type_graph=='6':
        return """'OverallQual', 'GrLivArea' and 'TotalBsmtSF' are strongly correlated with 'SalePrice'.
        'GarageCars' and 'GarageArea' are also some of the most strongly correlated variables.
        'GarageCars' and 'GarageArea' are like twin brothers. You'll never be able to distinguish them.
        Therefore, we just need one of these variables in our analysis (we can keep 'GarageCars' since its correlation with 'SalePrice' is higher).
        'TotalBsmtSF' and '1stFloor' also seem to be twin brothers.
        We can keep 'TotalBsmtSF' just to say that our first guess was right.
        'TotRmsAbvGrd' and 'GrLivArea', twin brothers again.
        Ah... 'YearBuilt'... It seems that 'YearBuilt' is slightly correlated with 'SalePrice'. """
    elif type_graph=='7':
        return """One of the figures we may find interesting is the one between 'TotalBsmtSF' and 'GrLiveArea'.
        In this figure we can see the dots drawing a linear line, which almost acts like a border.
        It totally makes sense that the majority of the dots stay below that line.
        Basement areas can be equal to the above ground living area, but it is not expected a basement area bigger than the above ground living area.

        The plot concerning 'SalePrice' and 'YearBuilt' can also make us think.
        In the bottom of the 'dots cloud', we see what almost appears to be a shy exponential function.
        We can also see this same tendency in the upper limit of the 'dots cloud'. 
        Also, notice how the set of dots regarding the last years tend to stay above this limit."""
    elif type_graph=='8':
        return "'SalePrice' is not normal. It shows 'peakedness', positive skewness and does not follow the diagonal line."
    elif type_graph=='9':
        return "'SalePrice' is not normal. It shows 'peakedness', positive skewness and does not follow the diagonal line."
    elif type_graph=='10':
        return "'GrLivArea' is not normal. It shows 'peakedness', positive skewness and does not follow the diagonal line."
    elif type_graph=='11':
        return "'GrLivArea' is not normal. It shows 'peakedness', positive skewness and does not follow the diagonal line."
    elif type_graph=='12':
        return """Something that, in general, presents skewness.
        A significant number of observations with value zero (houses without basement).
        A big problem because the value zero doesn't allow us to do log transformations."""
    elif type_graph=='13':
        return """Something that, in general, presents skewness.
        A significant number of observations with value zero (houses without basement).
        A big problem because the value zero doesn't allow us to do log transformations."""
    else:
        return "Error"
    
    