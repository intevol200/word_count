import matplotlib.pyplot as plt
import sys
import numpy as np

y = []

for freq in sys.stdin:
    a = freq.split()
    b = a[1]

    y.append(int(b))

plt.plot(range(1, len(y)+1), y)

plt.yscale("log")
plt.xscale("log")

plt.savefig('plot_figure.png')


# 지프의 법칙
first = 1
last = 1000
test = 500

s = (np.log(y[last-1]) - np.log(y[first-1])) / (np.log(last) - np.log(first))
c = y[first-1] + (s * first)

sys.stdout.write("s : ")
sys.stdout.write(str(-s))
sys.stdout.write(", c : ")
sys.stdout.write(str(c))
