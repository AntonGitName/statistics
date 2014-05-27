from math import sqrt
import random
import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from scipy.stats import chisquare, chi2
from scipy.stats.kde import gaussian_kde

m = 1000
n = 100
k = 10

y = []
for i in range(m):
    x = [random.randint(1, k) for i in range(n)]
    y.append(chisquare(x)[0])

mean_y, std_y = np.mean(y), np.std(y)
y = [(i - mean_y) / sqrt(np.std(y)) for i in y]
t = min(y)
y = [i - t for i in y]

pdf = gaussian_kde(y)
a = linspace(min(y), max(y), len(y) // 10)

fig, ax = plt.subplots(2, 1)
fig.subplots_adjust(wspace=0)

ax[0].plot(a, pdf(a))
ax[1].plot(a, chi2.pdf(a,k-1))

plt.show()
