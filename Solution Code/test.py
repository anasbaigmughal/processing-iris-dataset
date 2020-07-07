# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 10:37:53 2019

@author: Muhammad Anas Baig
"""

import pandas as pd #data structure
import numpy as np #ndimensional array or matrices, contains mathematical funtions for those arrays
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt #pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation:
from statistics import median 
from matplotlib import cm as cm
from matplotlib.colors import LinearSegmentedColormap



names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv('iris.data', names=names)
print(dataset)
#dataset.insert(0, 'New_ID', range(1, 1 + len(dataset)))


dataset = (dataset.set_index('class').T) # saving before
print(dataset.corr(method='pearson'))
#df = pd.DataFrame(dataset)

#Black is Val==1 & White is Val<1, to check diagnols are calculated correct
N = 150
Z = dataset.corr(method='pearson')
# G is a NxNx3 matrix
G = np.zeros((N,N,3))
# Where we set the RGB for each pixel
G[Z<1] = [1,1,1]
G[Z==1] = [0,0,0]
#plt.imshow(G)
cmap = LinearSegmentedColormap.from_list('mycmap', ['white', 'black'])
fig, ax = plt.subplots()
im = ax.imshow(G, cmap=cmap, interpolation='nearest')
fig.colorbar(im)
plt.title("Black is Val==1 & White is Val<1",fontweight="bold")
plt.show()


#Discretizing over Mean as B & W, Black is Val>Mean & White is Val<Mean
N = 150
Z = dataset.corr(method='pearson')
# G is a NxNx3 matrix
G = np.zeros((N,N,3))
# Where we set the RGB for each pixel
myMean = ((dataset.corr(method='pearson')).mean()).mean()
G[Z<myMean] = [1,1,1]
G[Z>myMean] = [0,0,0]
#plt.imshow(G)
cmap = LinearSegmentedColormap.from_list('mycmap', ['white', 'black'])
fig, ax = plt.subplots()
im = ax.imshow(G, cmap=cmap, interpolation='nearest')
fig.colorbar(im) 
plt.title("Discretizing over Mean as B & W",fontweight="bold")
plt.show()


#Assigning colours to values
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(dataset.corr(method = 'pearson'), vmin=-1, vmax=1)
fig.colorbar(cax)
plt.title("Coloured Graph Plot",fontweight="bold")
plt.show()


#plot correlation matrix
#fig = plt.figure()
#ax = fig.add_subplot(111)
#cax = ax.matshow(dataset.corr(), vmin=-1, vmax=1)
#cax = ax.matshow(dataset.corr(), vmin=-1, vmax=1)
#fig.colorbar(cax)
#ticks = np.arange(0,150,1)
#ax.set_xticks(ticks)
#ax.set_yticks(ticks)
#ax.set_xticklabels(names)
#ax.set_yticklabels(names)
#plt.show()

#print((dataset.corr(method='pearson')).mean())

#del dataset['class']
#median(dataset.corr(method='pearson'))
#dataset = dataset.drop(['class'], axis=1) 