from random import shuffle

def kth_1(x, k):
    if (len(x) == 1): return x[0]
    x5 = []
    for i in range((len(x) + 4)// 5):
        l = sorted(x[5*i:5*i+5])
        x5.append(l[(len(l) - 1) // 2])
    pivot = kth_1(x5, len(x5) // 2)
    left = [i for i in x if i < pivot]
    right = [i for i in x if i > pivot]
    if (k <= len(left)) :
        return kth_1(left, k)
    elif (k == len(left) + 1):
        return pivot
    else:
        return kth_1(right, k - len(left) - 1)

def kth_2(x, k):
    if (len(x) == 1): return x[0]
    pivot = x[0]
    left = [i for i in x if i < pivot]
    right = [i for i in x if i > pivot]
    if (k <= len(left)) :
        return kth_1(left, k)
    elif (k == len(left) + 1):
        return pivot
    else:
        return kth_1(right, k - len(left) - 1)

x = range(1,21)
shuffle(x)
print(x)
for i in sorted(x):
    print (kth_1(x, i), kth_2(x, i))
