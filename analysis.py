#pands-project work. Data exploration
#Author Jarlath Scarry

#we need to import a number of different libraries. Matplot lib provides valuable plotting functions, and seaborn helps us use some of these functions
import pandas as pd
import numpy as np
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


print('\033[1m' + 'Dataset head is shown below (first 5 rows of data):' + '\033[0m')
print(iris_df.head()) # exploring the dataset #https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d
print( )
time.sleep(3)
print('\033[1m' + 'Dataset shape (Rows,Columns):' + '\033[0m')
print(iris_df.shape)
print( )
time.sleep(3)
print('\033[1m' + 'Some dataset information is shown below:' + '\033[0m')
print(iris_df.info())
print( )
time.sleep(3)
print('\033[1m' + 'Dataset description will be shown below:' + '\033[0m')
print( )
time.sleep(3)
print("A summary of each of the variables will be output to the file variables.txt")
print( )
time.sleep(3)

print(iris_df.describe(include='all')) #https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d
with open('variables.txt', mode='w') as file_object: #open function returns the file as a file object. w mode means write mode
            print((iris_df.describe(include='all')), file=file_object) #the describe data is printed into the txt file
#https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file
#iris_df.describe(include='all').np.savetxt("variables.txt")
#file is closed automatically 
print( )
time.sleep(3)
print('\033[1m' + 'A histogram of each variable will be displayed and saved as variables_histogram.png' + '\033[0m')

#https://stackoverflow.com/questions/67300148/best-fit-to-a-histogramplot-iris
# make the 'species' column categorical to fix the order
iris_df['species'] = pd.Categorical(iris_df['species'])

fig, axs = plt.subplots(2, 2, figsize=(10, 5))
for col, ax in zip(iris_df.columns[:4], axs.flat):
    sns.histplot(data=iris_df, x=col, kde=True, hue='species', common_norm=False, legend=ax==axs[0,0], ax=ax)
    #sns.histplot(data=iris_df, x=col, kde=True, hue='species', common_norm=False, legend=ax==axs[0,0], ax=ax)
matplotlib.rcParams['toolbar'] = 'None' 
plt.tight_layout()
plt.savefig("variables_histogram.png") #save the figure in the directory as a .png file
plt.show()



#sns.scatterplot(data=iris_df, x = 'sepal_length', y = 'sepal_width' , hue = 'species', s = 50)
#plt.title('Comparison between sepal width and length on the basis of species')
#plt.savefig("iris_plot_1.png") #save the figure in the directory as a .png file. (first show the plot, then save it!)
#plt.show()


#sns.scatterplot(data=iris_df, x = 'petal_length', y = 'petal_width', hue = 'species', s= 50, marker = 'D') #https://www.youtube.com/watch?v=MB6eqJDFU9Q
#plt.title('Comparison between petal width and length on the basis of species')
#plt.savefig("iris_plot_2.png") #save the figure in the directory as a .png file. (first show the plot, then save it!)
#plt.show()

