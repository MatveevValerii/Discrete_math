import numpy as np
import math as mt
from numpy.polynomial import polynomial as p 
from numpy import array, zeros
from numpy.linalg import linalg as ln
import matplotlib.pyplot as mpl
import scipy as sc

#Polynomials a)
Pol1= [6, 1,-4, 1]
Roots_Pol = np.roots(Pol1)
print("Roots of polynomial are ", Roots_Pol)

#Polynomials b)
df = np.flip(Pol1)

b = p.polyder(df)
flipped_b= np.flip(b)
print("Roots of 1 derivative are", np.roots(flipped_b))

#Polynomials c)
start = -2
end = 1
plotstep = 0.1


Pol2 = np.flip(Pol1)
x = np.arange(start, end, plotstep)
c = p.polyval(x, Pol2)


l = np.roots(flipped_b)
c2 = p.polyval(x, b)

mpl.plot(x,c, label="Polynomial")
mpl.plot(x, c2, label="1 derivative")
mpl.plot(l, np.zeros(len(l)), 'r+', label= 'Roots of derivative')
#mpl.plot(0.41911132, 0, 'bo')
mpl.plot(Roots_Pol, np.zeros(len(Roots_Pol)), 'bo', label = 'Roots of polynomial')
mpl.legend()
mpl.grid()
mpl.show()

''
#Polynomials d)


a = np.sort(Roots_Pol)[-2]
b = np.sort(Roots_Pol)[-1]

squared_pol = p.polymul(Pol2, Pol2)

V_coef = p.polyint(squared_pol, scl=np.pi, lbnd= a)
V = p.polyval(b, V_coef)
print('d)\nVolume of the figure is\t',V)



#Matrices 

A = ([4.5, -2.3, 2.3],[2.3, 1.2, -4.2], [5.3, 2.7, 5.3])

A = np.array(A)
A= A.reshape((3,3))

B = ([55, 21 , 3], [4, 33, 2], [1, 2, 4])

B = np.array(B)
B = B.reshape((3,3))

#     a)

print('a)\nMatrix A transponded\n' ,np.transpose(A))

#     b)
AB = np.matmul(A,B)
print('b)\nAB\n', AB)

#     c)
BA = np.matmul(B, A)
print('c)\nAB = B', np.array_equal(AB,BA))

#     d)
print("d)\n(AB)^-1 = B^-1 A^-1 is\n", np.array_equal(np.transpose(AB), np.matmul(np.transpose(B), np.transpose(A))))

#     e)
eq = ([1, 1, -2, 1], [-2, 3, 4, -3], [1, 6, 0, -1], [1, 9, 0, -1])
reses= ([2,2,1,12])
print('e)\nSolutions are\n', ln.solve(eq, reses))