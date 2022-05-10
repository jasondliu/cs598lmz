import gc, weakref
from time import time
import cPickle as pickle

import numpy as np

from common import *
from spacegrad import *
from scipy.sparse import issparse, coo_matrix
from scipy.optimize import newton
from functools import reduce
from itertools import product, combinations
from spacegrad.utils import find_analog_indices
from math import pi, ceil
from math import sqrt as real_sqrt
from math import log as real_log
from utils import pd_reg
from ipdb import set_trace
from itertools import chain

from scipy.linalg import eig

# convenience Aliases for common numpy types and functions
# When numpy is aliased to nip(), these will be default names

# shorthands for numpy functions
log = np.log
sqrt = np.sqrt
exp = np.exp
concatenate = np.concatenate
asarray = np.asarray
isnan = np.isnan
isfinite = np.isfinite
isinf = np
