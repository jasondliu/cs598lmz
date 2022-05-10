import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x/5.0) * np.exp(x/10.0) + 5.0 * np.exp(-x/2.0)

def h(x):
    return int(f(x))

x = np.arange(1, 30, 0.1)

plt.plot(x, f(x))
plt.show()

res = minimize(h, 30, method='BFGS')

print(res.fun)
print(res.x)

res = minimize(h, 30, method='Nelder-Mead')

print(res.fun)
print(res.x)
