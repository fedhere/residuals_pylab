<a href="http://dx.doi.org/10.5281/zenodo.15419"><img src="https://zenodo.org/badge/10115/fedhere/residuals_pylab.svg"><a>

self explainatory: 

it makes a classical residual plot, with the residuals at the bottm and the data in the top panel. 
each plot can be scatter plot, line plot and the data can be errorbars

try it as follows

1.get 100 random numbers b/w 0 and 10
2.get the y as sine(x) plus some linear function of x with some scatter
3.get another array of 100 random numbers b/w 0 and 10
4.get the y for the second set as sine(x) plus some linear function, steeper this time, of x, with some scatter
5.get the residuals of a simple sine fit function (not a fit, just the sin(x)), as percentage
6.and finally plot it


here is the code:

import numpy as np

import pylab as pl

from residplot import plotwresids

x=np.random.rand(100)*10

y=np.sin(x)+0.3*(np.random.rand(100)-0.5)\*np.sqrt(x)

x1=np.random.rand(100)*10

y1=np.sin(x1)+(np.random.rand(100)-0.5)\*np.sqrt(x1)

res=(y-np.sin(x))

res1=(y1-np.sin(x1))

plotwresids(x,y,res,xlabel= "fake data",ylabel="sin-ish", legend="made up stuff")

plotwresids([x,x1],[y,y1],[res,res1],err=[None,np.sqrt(np.abs(np.sin(x1)))],xlabel= "fake data",ylabel="sin-ish",scatter=[True,True], color=['SteelBlue','DarkOrange'], legend=["madeup stuff","more madeup stuff"])

pl.show()

![alt tag](https://github.com/fedhere/residuals_pylab/blob/master/example1.png)

cite through DOI (see top)
