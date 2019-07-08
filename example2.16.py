import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

m = 2.67
alpha = 2.7
beta = 6.3
total_num = 1000
count = 0
Y = np.random.random(total_num)
U = m * np.random.random(total_num)
beta_pdf = stats.beta(alpha, beta).pdf(Y)

# # counting valid points
for i in range(total_num):
    if U[i]<=beta_pdf[i]:
        count+=1
print('count='+str(count))
print(str(100.0 * count/total_num)+'%')
plt.scatter(Y, U)

plt.scatter(Y, beta_pdf)
plt.xlabel('uniform[0,1]')
plt.ylabel('beta pdf')
plt.title('beta distribution accept-reject algorithm')
plt.show()