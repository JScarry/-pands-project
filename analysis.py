#pands-project work. Data exploration
#Author Jarlath Scarry

#we need to import a number of different libraries. Matplot lib provides valuable plotting functions, and seaborn helps us use some of these functions
import pandas as pd
import numpy as np
import matplotlib
#from matplotlib import rcParams
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid') #add a dark grid to the background of the plot
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (8, 4)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


#iris_df = pd.read_csv('IRIS.csv') #creating the data frame iris_df by reading in the file from the directory with pandas and
                                    #assigning it the variable iris_df
iris_df = sns.load_dataset("iris") #load iris dataset directly from seaborn

print(iris_df.head()) # exploring the dataset #https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d
print (iris_df.shape) # exploring the dataset 
print(iris_df.info())  # exploring the dataset. info is an interesting one, because it shows us there are no empty or null values. This could be helpful in some cases.

sns.scatterplot(data=iris_df, x = 'sepal_length', y = 'sepal_width' , hue = 'species', s = 50)
plt.title('Comparison between sepal width and length on the basis of species')
plt.savefig("iris_plot_1.png") #save the figure in the directory as a .png file. (first show the plot, then save it!)
plt.show()