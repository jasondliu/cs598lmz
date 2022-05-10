import ctypes
# Test ctypes.CFUNCTYPE(None) to replace the decorator
from ctypes import CFUNCTYPE, c_double, c_int, byref
from pybarst.barst import BARST # pylint: disable=no-name-in-module

user_func = CFUNCTYPE(None, c_double, c_double, ctypes.c_void_p)

def user_fn(t, y, p):
    """Defines the right-hand side of the differential equation."""
    # pylint: disable=unused-argument, no-value-for-parameter
    ydot = np.zeros([2]) # 2 states

    # y[0] - initial water level (m)
    # y[1] - initial water discharge (m^3/s)
    # t - time (s)
    # p[0] - minimum discharge (m^3/s)
    # p[1] - maximum discharge (m^3/s)
    # p[2] - maximum outlet elevation (m)
    # p[3] - maximum inlet elevation (m)
