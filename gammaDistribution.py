import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sps
from scipy.optimize import fsolve
from math import exp, log

##########################################
# use any positive numbers that you want #
shape, scale = 5., 1.73                  # 
##########################################

s = np.random.gamma(shape, scale, 1000)

def findParameters(x):
    x_a = sum(x) / len(x)
    x_g = exp(sum([log(i) for i in x]) / len(x))    
    t = x_a / x_g
    
    f = lambda x : (x - (t*exp(sps.digamma(x))))
    
    k = fsolve(f, 3)[0]  
    
    return k, x_a / k


my_k, my_theta = findParameters(s)



count, bins, ignored = plt.hist(s, 50, normed=True)

real_y = bins**(shape-1)*(np.exp(-bins/scale) / (sps.gamma(shape)*scale**shape))
my_y = bins**(my_k-1)*(np.exp(-bins/my_theta) / (sps.gamma(my_k)*my_theta**my_k))

plt.plot(bins, real_y, linewidth=2, color='r')
plt.plot(bins, my_y, linewidth=2, color='g')
plt.show()
