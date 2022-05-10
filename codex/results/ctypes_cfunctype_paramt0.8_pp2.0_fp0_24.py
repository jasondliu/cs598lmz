import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

fintegration = FUNTYPE(lib.test_sin)
#fintegration.restype=ctypes.c_double

print(fintegration(1.0))
from qutip import *
from math import *
import numpy as np
from scipy.integrate import *
from scipy.optimize import *

from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.special
import scipy.sparse.linalg as sla
import scipy.linalg as la
from scipy.integrate import complex_ode

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as
