import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H")).start()

import itertools
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spsl
import matplotlib.pyplot as plt

import pyamg

from pyamg.gallery import stencil_grid
from pyamg.gallery.diffusion import diffusion_stencil_2d

n = 100
stencil = diffusion_stencil_2d(type='FD',epsilon=0.001,theta=np.pi/3)
A = stencil_grid(stencil,(n,n),format='csr')

# solve Ax = b with a zero initial guess and zero boundary conditions
b = np.random.rand(A.shape[0])
x0 = np.zeros(A.shape[0])

# construct the multigrid hierarchy
ml = pyamg.ruge_stuben_solver(A)

# solve Ax = b to a relative tolerance of 1
