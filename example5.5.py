import numpy as np
import matplotlib.pyplot as plt
from math import *

def T(t):
    try:
        return 1/log(t)
    except Exception:
        return 1

def h(x):
    result = (cos(50*x)+sin(20*x))**2
    return result

def max(a,b):
    if a>=b:
        return a
    else:
        return b

def min(a,b):
    if a<=b:
        return a
    else:
        return b

def rho(u, x, t):
    result = min(exp((h(u)-h(x)) / T(t)), 1)
    return result

r = 0.5
iterations = 1000
X=[0]
T_list=[0]
H = [h(X[0])]
for t in range(iterations):
    at = max(X[t]-r, 0)
    bt = min(X[t]+r, 1)
    u = np.random.uniform(at,bt)
    # rand_choice = np.random.uniform(0,1)
    rand_choice = np.random.random()
    # print('randome_choice:',rand_choice)
    # print('u',u)
    if rand_choice<=rho(u,X[-1],t):
        X.append(u)
    else:
        X.append(X[t])

    T_list.append(T(t))
    H.append(h(X[-1]))

print(X[-1],H[-1])
print(sorted(H,reverse=True)[0])
plt.xlabel('Exploration')
plt.ylabel('Function Value')
plt.plot(X,H)
plt.show()
