from scipy.stats import norm
from scipy.stats.kde import gaussian_kde
import matplotlib.pyplot as plt
from numpy import linspace, random
import numpy as np

def uniform_kde(x):
    n, xmin = len(x), min(x)
    h = 10 * (max(x) - min(x)) / n
    indexes = range(1 + n / 10)
    y = [[] for i in indexes]
    for i in x: y[int((i-xmin) / h)].append(i)
    ni = [len(y[i]) for i in indexes]
    def f(t):
        return [ni[int((i-xmin) / h)] for i in t] / (n * h)
    return f   

mu, sigma, n = 0, 1, 1000
x = random.normal(0, 1, n)


pdf1 = gaussian_kde(x)
pdf2 = uniform_kde(x)

a = linspace(min(x), max(x), n * 10)

count, bins, ignored = plt.hist(x, n / 10, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')

plt.plot(a, pdf1(a), color='g')
plt.plot(a, pdf2(a), color='y')

plt.show()
