from scipy import stats 
import numpy as np
import matplotlib.pyplot as mpl

with open("data1.csv") as data_file:
    array = np.loadtxt(data_file, delimiter=" ")

res = stats.describe(array)

print('Average of results', res.mean)
print('Standart deviation', stats.tstd(array))
print('Range of variables \n', res.minmax[1]-res.minmax[0])


start = 0
end = 120
step = 1

x = np.arange(start, end, step)
for i in range(0,6):
    k=i+1
    mpl.plot(x,array[:,i], label=('variable '+str(k)))
    #mpl.plot(x,array[:,i], label=(k, 'variable'))
    mpl.xlabel('Row number')
    mpl.ylabel('Variable value')
    mpl.legend()
    mpl.grid()
    mpl.show()
    

#c.	Create a scatterplots of pairs of  variables.

mpl.scatter(array[:,0], array[:,1], s=6, label="1 and 2 variables")
mpl.legend()
mpl.grid()
mpl.show()

mpl.scatter(array[:,2], array[:,3], s=6, label="3 and 4 variables")
mpl.legend()
mpl.grid()
mpl.show()

mpl.scatter(array[:,4], array[:,5], s=6, label="5 and 6 variables")
mpl.legend()
mpl.grid()
mpl.show()