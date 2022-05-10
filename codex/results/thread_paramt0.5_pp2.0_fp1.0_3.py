import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()

import numpy as np
from scipy.optimize import minimize, approx_fprime, check_grad
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Зададим произвольную функцию
def f(x):
    return np.sin(x / 5.) * np.exp(x / 10.) + 5. * np.exp(-x / 2.)

# Зададим её производную
def f_prime(x):
    return np.cos(x / 5.) * np.exp(x / 10.) / 5. - np.sin(x / 5.) * np.exp(x / 10.) / 10. + 5. * np.exp(-x / 2.) / 2.

