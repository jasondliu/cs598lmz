import ctypes
# Test ctypes.CFUNCTYPE()
# A basic callback function.
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double))
def py_callback(x, array):
    array[0] = 666.0
    return x**2
# Convert the Python callback function into a C callback function.
c_callback = CALLBACKFUNC(py_callback)
# Create an array of 5 doubles, and pass it to the C callback.
d_array = (ctypes.c_double * 5)()
c_callback(12, d_array)
print d_array[0]

from ctypes import windll

def test_opt_dll():
    user32 = windll.user32
    k32 = windll.kernel32
    k32.GetCurrentThreadId()
    user32.GetDesktopWindow()
    k32.GetCurrentProcessId()
    k32.GetCurrentThreadId()
    user32.GetDesktopWindow()

#import matplotlib.pyplot as plt

