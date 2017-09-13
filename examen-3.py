#las librerias utilizadas
import matplotlib.pyplot as plt 
import numpy as np
#declaramos una funcion que nos devuelva f(x)=cos(2*x)*2015, donde el argumento del seno es la cantidad de anios que llevo en la universidad, y 2015 es cuando entre
def f(t):
 return  np.cos(2*t)*2015
#el rango de las variables
t1 = np.arange(0.0, 20.0, 0.0001)
t2=np.arange(0.0, 20.0, 0.0002)
#grafica t1 contra f(t1)
plt.plot(t1,f(t1), 'm')
plt.title('Funcion trigonometrica')

#crea el grupo de graficas
plt.figure(1)
#crea el lienzo con dos renglones, una columna y entra a la primera seccion de esta division
plt.subplot(211)
#grafica la variable t1 contra la funcion f(t1) con circulos azules y grafica la variable t2 contra la funcion f(t2) con una linea negra
plt.plot(t1, f(t1), 'yD', t2, f(t2), 'k')
#entra a la segunda seccion del lienzo dividido
plt.subplot(212)
#grafica la variable t2 contra la funsion cos
plt.plot(t2, np.cos(2*t2), 'r--')


#guarda la grafica
plt.savefig('examen3.png')
