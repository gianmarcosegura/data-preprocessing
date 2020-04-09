#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 01:03:54 2020

@author: gianmarcosegura
"""


# Datos faltantes

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

# Tratamiento de los datos 'NA': 
# axis 0 = column
# axis 1 = fila
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer.fit(X[:, 1:3])

X[:, 1:3] = imputer.transform(X[:, 1:3])