import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

"""
#lots of examples
import numpy as np
from numpy.ctypeslib import ndpointer
ctypes.get_errno()
# error: ndpointer() got an unexpected keyword argument 'shape'
ndarr = ndpointer(dtype=ctypes.c_double, shape=(1,1))
# error: ndpointer() got an unexpected keyword argument 'shape'
ndarr = ndpointer(dtype=ctypes.c_double, shape=(1,1), flags='WRITEABLE')
# ok
ndarr = ndpointer(dtype=np.float64, shape=(1,1), flags='WRITEABLE')
# ok
ndarr = ndpointer(dtype=np.float64, flags='WRITEABLE')
# also ok
ndarr = ndpointer(dtype=(np.float64), flags='WRITEABLE')
"""

