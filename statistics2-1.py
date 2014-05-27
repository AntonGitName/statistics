def mode(x):
	count = {y : x.count(y) for y in set(x)}
	return max((value, key) for key, value in count.items())[1]

def truncatedMean(x, k):
	return sum(sorted(x)[k:len(x) - k]) / (len(x) - 2 * k)

def WinzorMean(x, k):
	n = len(x)
	y = sorted(x)
	return (k * (y[k] + y[-k-1]) + sum(y[k:-k if k!= 0 else len(y)])) / len(x)
	
def printStatistics(x):
	n = len(x)
	sorted_x = sorted(x)

	print("mean[x] = {0}".format(sum(x) / n))
	
	median = (sorted_x[n // 2] + sorted_x[(n - 1) // 2]) / 2
	print("median[x] = {0}".format(median))
	
	print("mode[x] = {0}".format(mode(x)))
	
	iqm = 2 / n * (sum(sorted_x[n // 4 : 3 * n // 4]))
	print("InterQuartileMean[x] = {0}".format(iqm))
	
	print("ExtremeSum[x] = {0}".format((sorted_x[0] + sorted_x[-1]) / 2))
	
	print("VinzorMean[x] = {0}".format(WinzorMean(x, 2)))
	
	print("TruncatedMean[x] = {0}".format(truncatedMean(x, 2)))
	
printStatistics([0.0, 2.0, 1.0, 4.0, 1.0, 1.0, 0.0, 0.0, 0.0, 5.0, 1.0, 1.0, 1.0, 2.0, 1.0, 0.0, 2.0, 1.0, 4.0, 1.0])