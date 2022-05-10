import threading
threading.stack_size(2**27)
import sys
import time
import math
import numpy as np
from numpy import zeros, ones, array, linspace, logspace
from numpy.linalg import norm
from scipy.sparse import csr_matrix, lil_matrix
from scipy.sparse.linalg import spsolve
from matplotlib import pyplot as plt
from scipy.sparse.linalg import cg
from mpl_toolkits.mplot3d import Axes3D

from pylab import show, figure
import scipy
from scipy import stats
from sympy import *
from sympy import Matrix
from sympy.abc import *

from scipy.sparse.linalg import cg
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from sympy.printing import jscode

from mpl_toolkits.mplot3d
