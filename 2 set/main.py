from scipy import stats 
import numpy as np
import matplotlib.pyplot as mpl
from scipy.stats import linregress

Bl_pres= ([1, 0, 1, 2, 5, 1, 4, 6, 2, 3], [5, 4, 6, 8, 4, 5, 7, 9, 7, 6])
Noise = ([60, 63, 65, 70, 70, 70, 80, 90, 80, 80], [85, 89, 90, 90, 90, 90, 94, 100, 100, 100])

Bl_pres =np.array(Bl_pres)
Noise = np.array(Noise)

Bl_pres = np.reshape(Bl_pres, 20)
Noise = np.reshape(Noise, 20)




step = 1

x= np.arange(0, len(Noise), step)

y = np.column_stack((Noise, Bl_pres))
#y = np.reshape(y, ((3, 20)), 'A')
y=np.transpose(y)
r = np.corrcoef(y, rowvar=True)


line = stats.linregress(Noise, Bl_pres)
#print(f'y={line.slope:.3f}x {line.intercept:.3f}') formula of the line

mpl.scatter(Noise, Bl_pres, s=8, label="Blood pressure vs noise")
mpl.plot(Noise, line.slope*Noise + line.intercept, 'tab:orange', label = 'Fitted line')
mpl.legend()
mpl.grid()
mpl.show()

Noise_level = 90
print('Matrice of corr coefficients is \n', r)
print('Answer to part e (noise level=90) ',round(line.slope*Noise_level+line.intercept,4))

print('Answer to part f', (5-line.intercept)/line.slope)
