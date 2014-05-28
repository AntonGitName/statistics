from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfinv
from scipy.optimize import fsolve
n, m, p = 1000, 1000, 0.35

x = sorted([np.mean(np.random.geometric(p, n)) for i in range(m)])

eps = 0.005

left_x, right_x = x[int(m * eps / 2)], x[int(m * (1 - eps / 2))]

def theoretic_interval(x, eps):
    mean = np.mean(x)
    k = (erfinv(eps / 2))**2 / len(x)
    a, b, c = mean**2, (k - 2 * mean), 1 - k
    
    return (-b-sqrt(b**2-4*a*c))/(2*a), (-b+sqrt(b**2-4*a*c))/(2*a)

print(1 / right_x, 1 / left_x)

print(theoretic_interval(np.random.geometric(p, n), eps))

