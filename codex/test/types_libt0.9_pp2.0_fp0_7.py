import types
types.slice = slice

# -----------------------------------------------------------------------------
# Imports: external
# -----------------------------------------------------------------------------
import numpy as np
import numpy.linalg as la

# -----------------------------------------------------------------------------
# Code
# -----------------------------------------------------------------------------

def isint(s):
    """ Is s an integer string? """
    try:
        int(s)
    except:
        return False
    return True

def toint(s):
    """ Convert to int, returning 0 if fails """
    try:
        i = int(s)
    except:
        i = 0
    return i

def set2str(s):
    """ Return a sorted comma-separated list of values """
    return ','.join(sorted(str(i) for i in s))

def str2array(a):
    """ Convert a string to a NaN-separated Numpy array of floats """
    try:
        b = np.array(a.split(','), dtype=np.float32)
    except:
        b = np.array([])
    return b

