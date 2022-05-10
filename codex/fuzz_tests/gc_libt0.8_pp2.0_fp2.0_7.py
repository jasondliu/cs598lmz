import gc, weakref, sys, inspect, os
from jitcode import y,t
from RHS import get_RHS, free_RHS
from numba import jit
from scipy.sparse import csr_matrix

from core.backward_euler import BackwardEuler


from numpy.core.fromnumeric import ravel_multi_index, unravel_index
from numpy.core.fromnumeric import shape as npshape
from numpy.core.fromnumeric import reshape as npreshape
from numpy.core.fromnumeric import size as npsize
from numpy.core.fromnumeric import swapaxes as npswapaxes
from numpy.core.fromnumeric import squeeze as npsqueeze
from numpy.core.fromnumeric import transpose as nptranspose
from numpy.core.fromnumeric import copy as npcopy
from numpy.core.fromnumeric import concatenate as npconcatenate
from numpy.core.fromnumeric import diag as npdiag
from numpy.core.
