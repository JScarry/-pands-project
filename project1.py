#pands-project work. Data exploration
#Author Jarlath Scarry
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

irisDf = pd.read_csv('iris.csv')
irisDf.info()

print(irisDf.head())

print (irisDf.shape) # explore dataset

