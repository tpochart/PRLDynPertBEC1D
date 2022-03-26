import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def rhs(n,t,a=1):
    #n : Array of coordinates n_k
    #a : 4*Gamma_eff/L in PhysRevA
    N=len(n)
    R=[0]*N #To return
    for k in range(N):
        s=0
        for q in range(N):
           s+=((np.sin(k)-np.sin(q))**2)*n[k]*n[q]
        R[k]=-a*s
    return(R)

def plot_(list_n_ini, funcs=[], t_ini=0, t_fin=100, nb_t=10000, displayed_sites=[], a=1):
    # We plot for multiple n_ini ; nb_sites is built-in in the len(n_ini[i]), which are assumed to all be the same
    # kwarg funcs : optionally, other functions to be plotted for comparison
    # kwargs t_ini, t_fin, t_nb : settings for t linspace
    # kwarg displayed_sites : choose which n_k to display (if a n_k is displayed, then it is displayed for all n_ini). [] means displaying all sites.
    # kwarg a : a for rmb
    if displayed_sites==[]:
        displayed_sites = list(range(len(list_n_ini[0])))
    t = np.linspace(t_ini,t_fin,nb_t)
    plt.xscale('log')
    plt.yscale('log')
    for n_ini in list_n_ini:
        n = odeint(rhs, n_ini, t, args=(a,))
        for i in displayed_sites:
            plt.plot(t, np.array([x[i] for x in n]),label=f'$n_'+str(i)+'$'+r', $n_{ini}$='+str(n_ini))
    plt.legend()
    plt.show()
            
