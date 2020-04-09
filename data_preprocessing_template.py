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