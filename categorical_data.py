#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 01:01:06 2020

@author: gianmarcosegura
"""


# Datos categoricos

# Como importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Data.csv')

# Dividimos los datos en 2.
# x serán las variables independientes.
# y serán las variables dependientes.
# .iloc: el primer parámetro seleciona las filas que quieres,
# el segundo las columnas que quieres
# con ':' a la izquierda se indica el inicio y a la derecha el final, 
# si no pones nada te coje todo
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3]


# Codificar a datos categoricos
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
onehotencoder = make_column_transformer((OneHotEncoder(), [0]), remainder = "passthrough")
X = onehotencoder.fit_transform(X)



# Codificar a datos ordinales
from sklearn import preprocessing
labelencoder_Y = preprocessing.LabelEncoder()
y = labelencoder_Y.fit_transform(y)