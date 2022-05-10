import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"
# %load_ext cython

#%load_ext line_profiler

