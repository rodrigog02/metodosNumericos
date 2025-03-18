import numpy as np
import matplotlib.pyplot as plt


def fx(x):
    return x / np.cbrt(4 + x**2)
a = 2
b = 8
n = 6

h= (b-a)/n
xi = a
suma = fx(xi)
for i in range(0,n-1,1):
    xi = xi + h
    suma = suma + 2*fx(xi)
suma = suma + fx(b)
area = h*(suma/2)    

print('trapecios:', n)
print('integral:', area)


#GRAFICA
#puntos de miuestra
muestras = n + 1
xi = np.linspace(a,b,muestras)
fi = fx(xi)
# linea suave
muestraslinea= n*10 + 1
xk = np.linspace(a,b,muestraslinea)
fk = fx(xk)
# graficando
plt.plot(xk,fk, label = 'f(x')
plt.plot(xi,fi, marker='o',
         color='orange', label = 'muestras')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('integral: regla de trapecios')
plt.legend()

# Trapecios
plt.fill_between(xi,0,fi, color='g')
for i in range(0,muestras,1):
    plt.axvline(xi[i], color='w')
plt.show()    
