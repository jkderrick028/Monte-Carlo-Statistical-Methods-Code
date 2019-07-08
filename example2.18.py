import matplotlib.pyplot as plt
from scipy import integrate
import scipy.stats as stats
import numpy as np

alpha = 2.1
total_num = 50000
# M = np.sqrt(2.0*np.pi/np.e)
M = 1.3
lb = -5
hb = 5

def g(x):
    result = (alpha/2)*np.exp(-alpha*np.abs(x))
    return result

def f(x):
    result = (1.0/np.sqrt(2 * np.pi))*np.exp(-x**2/2.0)
    return result

def bound(x):
    result = np.sqrt(2.0/np.pi)*(1.0/alpha)*(np.exp(alpha**2/2.0))
    return result

def g_pdf():
    res,_ = integrate.quad(g,lb,hb)
    return res

X = np.linspace(lb,hb,total_num)
U = stats.uniform(0,1).pdf(X)
norm_pdf = stats.norm(0,1).pdf(X)
laplace_pdf = stats.laplace.pdf(X)
Y = list()
X_y = list()

for i in range(total_num):
    if U[i] <= f(laplace_pdf[i])/(M*g(laplace_pdf[i])):
        Y.append(laplace_pdf[i])
        X_y.append(X[i])
    else:
        continue

print(g_pdf())
plt.scatter(X_y, Y)
plt.scatter(X, norm_pdf)
plt.title('example2.18')
plt.show()
