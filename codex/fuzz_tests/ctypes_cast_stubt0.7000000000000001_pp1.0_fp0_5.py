import ctypes
ctypes.cast(0, ctypes.py_object)

# This is a bit faster.
ctypes.pythonapi.PyCObject_FromVoidPtr.restype = ctypes.py_object
ctypes.pythonapi.PyCObject_FromVoidPtr.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]

def new_handle(space, w_subtype, w_args):
    return ctypes.pythonapi.PyCObject_FromVoidPtr(
        space.interp_w(W_Root, space.call_args(w_subtype, w_args)),
        None)

def unwrap_handle(space, w_handle):
    return ctypes.pythonapi.PyCObject_AsVoidPtr(w_handle)

def descr_new_handle(space, w_subtype
