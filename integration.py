import numpy as np
from math import *

n = 10**5
X = np.random.uniform(0,1,n)
Y = np.random.uniform(0,1,n)

def f(x):
    result = (1/sqrt(2*pi))*(exp(-(x**2)/2))
    return result

count =0
for i in range(n):
    if Y[i]<=f(X[i]):
        count+=1

print(count/n)

