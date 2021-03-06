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

def plot_(list_n_ini, funcs=[], funcs_names=[], t_ini=0, t_fin=100, nb_t=10000, displayed_sites=[], a=1):
    # We plot selected n_k for multiple n_ini ; nb_sites is built-in in the len(n_ini[i]), which are assumed to all be the same
    # kwarg funcs : optionally, other functions to be plotted for comparison
    # kwarg funcs_names: name of the other functions, to put in labels
    # kwargs t_ini, t_fin, t_nb : settings for t linspace
    # kwarg displayed_sites : choose which n_k to display (if a n_k is displayed, then it is displayed for all n_ini). [] means displaying all sites.
    # kwarg a : a for rhs
    if displayed_sites==[]:
        displayed_sites = list(range(len(list_n_ini[0])))
    t = np.linspace(t_ini,t_fin,nb_t)
    plt.xscale('log')
    plt.yscale('log')
    for n_ini in list_n_ini:
        n = odeint(rhs, n_ini, t, args=(a,))
        for i in displayed_sites:
            plt.plot(t, np.array([x[i] for x in n]),label=f'$n_'+str(i)+'$'+r', $n_{ini}$='+str(n_ini))
    for i in range(len(funcs)):
            plt.plot(t, funcs[i](t),label=funcs_names[i])
    plt.xlabel('t')
    plt.legend()
    plt.show()
            
def plot_tot(list_n_ini, funcs=[], funcs_names=[], t_ini=0, t_fin=100, nb_t=10000, displayed_sites=[], a=1):
    # We plot the total number of bosons for multiple n_ini ; nb_sites is built-in in the len(n_ini[i]), which are assumed to all be the same
    # kwarg funcs : optionally, other functions to be plotted for comparison
    # kwarg funcs_names: name of the other functions, to put in labels
    # kwargs t_ini, t_fin, t_nb : settings for t linspace
    # kwarg a : a for rhs
    if displayed_sites==[]:
        displayed_sites = list(range(len(list_n_ini[0])))
    t = np.linspace(t_ini,t_fin,nb_t)
    plt.xscale('log')
    plt.yscale('log')
    for n_ini in list_n_ini:
        n = odeint(rhs, n_ini, t, args=(a,))
        plt.plot(t, np.array([sum(x) for x in n]),label=r'$n_{tot}$'+r', $n_{ini}$='+str(n_ini))
    for i in range(len(funcs)):
            plt.plot(t, funcs[i](t),label=funcs_names[i])
    plt.xlabel('t')
    plt.legend()
    plt.show()

# Some functions and their names that we'll use for comparison

def func1(t):
    return(1/t)

func1_name = r'1/t'

def func2(t):
    return(1/np.sqrt(t))

func2_name = r'$1/\sqrt{t}$'
