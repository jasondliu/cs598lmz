import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

from scipy.integrate import odeint
from scipy.optimize import fsolve

from matplotlib import rc
import matplotlib as mpl
rc('font',**{'family':'serif','serif':['Times'],'size':10})
rc('text', usetex=True)

import time

def get_rhs(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
