import ctypes
ctypes.cast(0, ctypes.py_object)

# This is required to be able to use the c-implementation of the PicklingTools
# module. Otherwise, it will use the python implementation of the
# PicklingTools module.
# See: https://github.com/SciTools/cartopy/issues/845
import pickle
pickle.loads = ctypes.pythonapi.PyObject_CallMethod
pickle.loads.restype = ctypes.py_object
pickle.loads.argtypes = (ctypes.py_object, ctypes.c_char_p, ctypes.py_object)
