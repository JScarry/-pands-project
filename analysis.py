#pands-project work. Data exploration
#Author Jarlath Scarry

#we need to import a number of different libraries. Matplot lib provides valuable plotting functions, and seaborn helps us use some of these functions
import pandas as pd
#import numpy as np
import matplotlib
#from matplotlib import rcParams
import matplotlib.pyplot as plt
import seaborn as sns
import time

sns.set_style('darkgrid') #add a dark grid to the background of the plot
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (8, 4)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


iris_df = pd.read_csv('IRIS.csv') #creating the data frame iris_df by reading in the file from the directory with pandas and
                                    #assigning it the variable iris_df
#iris_df = sns.load_dataset("iris") #load iris dataset directly from seaborn
 
print()
print('\033[1m' + 'Dataset head is shown below (first 5 rows of data):' + '\033[0m')
print()
print(iris_df.head()) # exploring the dataset #https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d
print( )
time.sleep(3)

print('\033[1m' + 'Dataset shape (Rows,Columns):' + '\033[0m')
print(iris_df.shape)
print()
time.sleep(3)

print('\033[1m' + 'Dataset information summary is shown below:' + '\033[0m')
print(iris_df.info())
print()
time.sleep(3)

print('\033[1m' + 'Dataset description will be shown below:' + '\033[0m')
print()
time.sleep(3)
print('\033[1m' + 'A summary of each of the variables will be output to the file variables.txt' + '\033[0m')
print()
time.sleep(3)

print(iris_df.describe(include='all')) #https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d
with open('variables.txt', mode='w') as file_object: #open function returns the file as a file object. w mode means write mode
            print((iris_df.describe(include='all')), file=file_object) #the describe data is printed into the txt file
#https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file
#iris_df.describe(include='all').np.savetxt("variables.txt")
#file is closed automatically 


#https://stackoverflow.com/questions/67300148/best-fit-to-a-histogramplot-iris
# make the 'species' column categorical to fix the order
#iris_df['species'] = pd.Categorical(iris_df['species'])
print()
print('\033[1m' + 'Histograms of the variables will be displayed and saved as variables_histogram.png' + '\033[0m')
time.sleep(3)
print('\033[1m' + 'Figure will be displayed for 1 minute.' + '\033[0m')
time.sleep(3)
print('\033[1m' + 'When you have finished viewing press ANY KEY to close it and continue.' + '\033[0m')
time.sleep(3)

fig, axs = plt.subplots(2, 2, figsize=(10, 5))
for col, ax in zip(iris_df.columns[:4], axs.flat):
    sns.histplot(data=iris_df, x=col, hue='species', common_norm=False, legend=ax==axs[0,0], ax=ax)
    matplotlib.rcParams['toolbar'] = 'None' #remove the toolbar from the top of the display
plt.tight_layout()
plt.savefig("variables_histogram.png") #save the figure in the directory as a .png file
plt.waitforbuttonpress(60)
plt.close()

print()
print('\033[1m' + 'Scatterplots of the variables will be displayed and saved as variables_pairplot.png' + '\033[0m')
time.sleep(3)
print('\033[1m' + 'Figure will be displayed for 1 minute.' + '\033[0m')
time.sleep(3)
print('\033[1m' + 'When you have finished viewing press ANY KEY to close it and continue.' + '\033[0m')
print()
time.sleep(3)

sns.pairplot(data = iris_df,hue="species",height=3)
plt.savefig("variables_pairplot.png") #save the figure in the directory as a .png file
plt.waitforbuttonpress(60) #https://www.geeksforgeeks.org/matplotlib-pyplot-waitforbuttonpress-in-python/
plt.close()

print('\033[1m' + 'An approximation of sepal and petal areas will be calculated' + '\033[0m')
time.sleep(3)
print('\033[1m' + 'Area columns will be added and saved to a new file IRIS2.csv' + '\033[0m')
time.sleep(3)
print('\033[1m' + 'A summary of the new file IRIS2.csv and Figure will be displayed for 1 minute' + '\033[0m')
time.sleep(3)
print('\033[1m' + 'When you have finished viewing press ANY KEY to close it and continue.' + '\033[0m')
print()
time.sleep(3)

def area_function(): #defined function to do calculations and add new columns to the dataframe 
    areas_calculation = (iris_df["sepal_length"] * iris_df["sepal_width"])/2 #https://www.w3schools.com/python/pandas/ref_df_sum.asp
    iris_df["sepal_area"] = areas_calculation
    areas_calculation = (iris_df["petal_length"] * iris_df["petal_width"])/2
    iris_df["petal_area"] = areas_calculation



area_function()
iris_df.to_csv("IRIS2.csv")

print(iris_df.shape)
print()
print(iris_df.head())
print()
time.sleep(3)

plt.title('Comparison between sepal and petal areas')
sns.scatterplot(data=iris_df, x = 'sepal_area', y = 'petal_area' , hue = 'species', s = 50)
plt.savefig("area_scatterplot.png")
plt.waitforbuttonpress(60)
plt.close()
print()

print('\033[1m' + 'END' + '\033[0m')