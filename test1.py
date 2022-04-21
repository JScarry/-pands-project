
#https://stackoverflow.com/questions/67300148/best-fit-to-a-histogramplot-iris
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
import pandas as pd
import time
import sys



sns.set()
iris = sns.load_dataset('iris')
# make the 'species' column categorical to fix the order
#iris['species'] = pd.Categorical(iris['species'])

print('\033[1m' + 'Histograms of the variables will be displayed and saved as variables_histogram.png' + '\033[0m')
time.sleep(3)
print('\033[1m' + 'Figure will be displayed for 30 seconds.' + '\033[0m')
time.sleep(3)
print('\033[1m' + 'When you have viewed the chart press ANY KEY to close it and continue.' + '\033[0m')
time.sleep(3)

fig, axs = plt.subplots(2, 2, figsize=(12, 6))
for col, ax in zip(iris.columns[:4], axs.flat):
    # kde=False , x=col
    sns.histplot(data=iris, x=col, hue='species', common_norm=True, legend=ax==axs[0,0], ax=ax)
plt.tight_layout()
#plt.show(block=False)
#plt.pause(5) #https://stackoverflow.com/questions/40395659/view-and-then-close-the-figure-automatically-in-matplotlib
time.sleep(3)
plt.waitforbuttonpress(30)
plt.close()
print('\033[1m' + 'END' + '\033[0m')
