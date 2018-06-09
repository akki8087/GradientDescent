# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:27:35 2018

@author: NP
"""

import pandas as pd
import numpy as np

data = pd.read_csv('ex1data1.txt',names = ['x','y'])

X = data.iloc[:,:1]
y = data.iloc[:,-1:]

alpha = 0.01
X.insert(0, 'one', 1, allow_duplicates=True)
n = 1500

theta = np.array([[0.0], [0.0]])

def GD(X,y,theta,alpha,n):
    i = 0
    cost = []
    m = len(X)
    while i < n:
        
        y_pred = pd.DataFrame(np.dot( X,theta))
    
        cost.append(sum((y['y'] - y_pred[0])**2)/(2*m))
    
        temp0 = theta[0] - (alpha*(sum(y_pred[0] - y['y']))/m)
        temp1 = theta[1] - (alpha*(sum((y_pred[0] - y['y'])*X.iloc[:,1])/m))
        
        theta[0] = temp0
        theta[1] = temp1
        
        i += 1
    return theta

GD(X,y,theta,alpha,n)

