import numpy as np
from math import *

def g(x):
    result = exp((-x**2)/2)/sqrt(2*pi)
    return result

def f(y):
    result = (g((b-a)*y+a)-c)/(d-c)
    return result

n = 10**5
X = np.random.uniform(0,1,n)
Y = np.random.uniform(0,1,n)
a = 2
b = 5
c = g(5)
d = g(2)
count = 0
J0 = (a-b)*(c-d)
J1 = c*(b-a)

for i in range(n):
    if Y[i]<=f(X[i]):
        count+=1

print(count)
integral = J0*count/n + J1
print(integral)
