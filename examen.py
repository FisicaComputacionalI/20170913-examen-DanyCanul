#las librerias que se utilizan
import numpy as np
import pylab as pl 
#Vector con los valores del eje x
x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#Vector con los valores del eje y
y=[1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
#Grafica el vector x contra el vector y, el color y tipo de linea
pl.plot(x,y, 'yD')
#pongo la misma idicacion para que se grafique solo la linea de la grafica
pl.plot(x,y, 'k')
#Titulos a los ejes y la grafica
pl.xlabel('Edad')
pl.ylabel('Anio')
pl.title('Daniela Canul Garcia')
#Guarda la grafica
pl.savefig('examen1.png')


