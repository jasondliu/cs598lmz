import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ord(b'a')
use_pure_python = 0
if use_pure_python == 0:
    import sys
    import numpy as np
    from scipy.integrate import odeint
