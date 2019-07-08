import numpy as np
import matplotlib.pyplot as plt

m = 1000
runs = 100

def delta(k):
    theta = [np.random.normal(10, 1) for _ in range(k)]
    numerator=0
    denominator = 0
    for i in range(k):
        numerator+=theta[i]/(1+theta[i]**2)
        denominator+=1/(1+theta[i]**2)
    return numerator/denominator

x_list = []
y_list = []
for i in range(m):
    for run in range(runs):
        x_list.append(i+1)
        y_list.append(delta(i+1))

plt.xlim(0,1000)
plt.ylim(9.5,10.8)
plt.scatter(x_list,y_list)
plt.show()

