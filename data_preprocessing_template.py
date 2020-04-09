# -*- coding: utf-8 -*-
"""
@author: Gianmarco Segura

"""

# Plantilla de Pre Procesado

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


# Útil para variables categóricas
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
onehotencoder = make_column_transformer((OneHotEncoder(), [0]), remainder = "passthrough")
X = onehotencoder.fit_transform(X)


# Dividir el data set en conjunto de entrenamiento y conjunto de tenting
# random_state > numero aleatorio para que te devuelva aleatoriamente unos valores a probar
# test_size

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Escalado de variables

"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""






