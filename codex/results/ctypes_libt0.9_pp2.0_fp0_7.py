import ctypes
ctypes.cdll.LoadLibrary('Atlas.dll')
import numpy.ctypeslib as npct
import array as arr
import matplotlib.pyplot as plt
import os

Asf2 = npct.load_library('Atlas.dll', '.')
Asf2.Set_Verbose.restype = None
Asf2.Set_Verbose.argtypes = [ ctypes.c_bool ]

# SE = ctypes.CDLL('Ser_lib.so')
# SE.Set_Verbose.argtypes = [ ctypes.c_bool ]

# SE.Set_Verbose(True)

# N = 6    # order of the transfer function  
# n = 2    # order of the numerator polynomial
# m = N - n
# wn = .3 + .5j    # natural frequency: .5 discriminant, abs(wn) = .5
# z = .2 + .2j     # zeta: .4 discriminant, abs(z) = .4
# wn = .5    # natural frequency
# z
