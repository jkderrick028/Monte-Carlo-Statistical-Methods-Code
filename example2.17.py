from scipy import integrate
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
lb = -4
hb = 4
total_num = 5000
valid_num = 0

def f(x):
    return np.exp(-x*x/2)*(np.sin(6*x)*np.sin(6*x)+3*np.cos(x)*np.cos(x)*np.sin(4*x)*np.sin(4*x)+1)

def f_pdf(x):
    res,_ = integrate.quad(f, lb, hb)
    # return f(x)
    return f(x)/res

rs,_ = integrate.quad(f_pdf, lb, hb)
# print(rs)

X = np.linspace(lb, hb, total_num)
Y = f(X)
M = np.max(Y)
# print(M)
norm_pdf = stats.norm(0,1).pdf(X)
norm_pdf = 5 * np.sqrt(2*np.pi) * norm_pdf

for i in range(total_num):
    if norm_pdf[i]>=Y[i]:
        valid_num+=1
print('support: ',end='')
print(str(100.0*valid_num/total_num)+'%')
plt.scatter(X,Y)
plt.scatter(X, norm_pdf)
plt.title('Example 2.17')
plt.show()

