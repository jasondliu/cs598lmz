import ctypes
ctypes.cast(None, ctypes.py_object)

import numpy as np 
import numpy.ctypeslib as npct 
array_1d_double = npct.ndpointer(dtype=np.double, ndim=1, flags='CONTIGUOUS') 

