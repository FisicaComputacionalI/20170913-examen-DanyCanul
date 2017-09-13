#las librerias utilizadas
import matplotlib.pyplot as plt 
import numpy as np
#declaramos una funcion que nos devuelva f(x)=sen(2*x)*2015, donde el argumento del seno es la cantidad de anios que llevo en la universidad, y 2015 es cuando entre
def f(t):
 return  np.cos(2*t)*2015
#el rango de las variables
t1 = np.arange(0.0, 20.0, 0.0001)
#grafica t1 contra f(t1)
plt.plot(t1,f(t1), 'm')
plt.title('Funcion trigonometrica')
#guarda la grafica
plt.savefig('examen2.png')
