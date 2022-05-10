import sys, threading
threading.Thread(target=lambda: (sys.stdout.write('\r'), sys.stdout.flush())).start()
# This is only needed if you want to do some basic telemetry (counters/timers)
# https://docs.python.org/3/library/threading.html#thread-objects
# https://docs.python.org/3/library/threading.html#timer-objects
import time
tic = time.time()

import numpy as np
np.__version__

# linear algebra
import scipy.linalg as sla
# compare floating-point values
from numpy.testing import assert_allclose
# sparse matrices
import scipy.sparse as sps
from scipy.sparse import csr_matrix, csc_matrix, coo_matrix
# graph algorithms
import scipy.sparse.csgraph as csgraph

import matplotlib
import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_style("darkgrid")
# sns.set_palette("colorblind
