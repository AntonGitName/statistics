from scipy.stats import norm
from scipy.stats.kde import gaussian_kde
import matplotlib.pyplot as plt
from numpy import linspace, random
import numpy as np

def uniform_kde(x):
    n, xmin, d = len(x), min(x), (max(x)-min(x))*1.000001
    if (n > 10):
        h = 10 * d / n
    else:
        h = d
    k = int(d / h)
    ni = [0 for i in range(k)]
    for i in x: ni[int((i-xmin) / h)] += 1
    def f(t):
        return [ni[int((i-xmin) / h)] for i in t] / (n * h)
    return f   

mu, sigma, n = 0, 1, 100
x = random.normal(0, 1, n)


pdf1 = gaussian_kde(x)
pdf2 = uniform_kde(x)

a = linspace(min(x), max(x), n * 10)

count, bins, ignored = plt.hist(x, (n + 9) / 10, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='y')

plt.plot(a, pdf1(a), color='g')
plt.plot(a, pdf2(a), linewidth=3,color='r')

plt.show()
