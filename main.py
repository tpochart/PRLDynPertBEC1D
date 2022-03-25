import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

a = 1 #4 Gamma_eff / L in PhysRevA

def rmb(n,t):
    #n : Array of coordinates n_k
    N=len(n)
    R=[0]*N #To return
    for k in range(N):
        s=0
        for q in range(N):
           s+=((np.sin(k)-np.sin(q))**2)*n[k]*n[q]
        R[k]=-a*s
    return(R)

def plot_multin(n_ini):
    #Number of lattice sites built-in in the n_ini arg
    t = np.linspace(0,100,10000)
    n = odeint(rmb, n_ini, t)
    plt.xscale('log')
    plt.yscale('log')
    for i in range(len(n[0])):
        plt.plot(t, np.array([x[i] for x in n]),label=f'$n_'+str(i)+'$')
    plt.legend()
    plt.show()

def plot_multiini(list_n_ini_0,nb_sites):
    t = np.linspace(0,100,10000)
    plt.xscale('log')
    plt.yscale('log')
    for n_ini_0 in list_n_ini_0:
        n_ini = [n_ini_0]*nb_sites
        n = odeint(rmb, n_ini, t)
        plt.plot(t, np.array([x[0] for x in n]),label=str(n_ini_0))
    plt.legend()
    plt.show()
