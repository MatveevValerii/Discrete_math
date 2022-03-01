from scipy import stats 
import numpy as np
import matplotlib.pyplot as mpl

Upeak = 10 
Ipeak = 5 
phi_u= np.pi/2
phi_i = np.pi/6
n = 2 

T = 0.02



t_start = 0
t_end = n*T
step = 0.0001

t = np.arange(t_start, t_end, step)

u = Upeak*np.sin(100*np.pi*t+phi_u)
i = Ipeak*np.sin(100*np.pi*t+phi_i)

Pave = (1/2)*Upeak*Ipeak*np.cos(phi_u-phi_i)

p =  u*i

fig, axs = mpl.subplots(2)

axs[0].plot(t, u, 'tab:red', label="u(t)")
axs[0].plot(t, i, 'tab:green', label= "i(t)", )
axs[0].set_title('Voltage and current')
axs[0].legend()
axs[0].grid()

Pave_arr = np.full(len(t), Pave)

axs[1].plot(t, p, 'tab:orange', label= "Momentary power")
axs[1].plot(t, Pave_arr, 'tab:blue',  label= "Average power", )
axs[1].set_title('Momentary and average power')
axs[1].legend()
axs[1].grid()

fig.tight_layout()
mpl.show()
