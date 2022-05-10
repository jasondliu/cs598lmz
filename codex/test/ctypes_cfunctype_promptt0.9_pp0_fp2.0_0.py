import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_int)(funcPtr)

def fProperty(fGet, fSet = None, fDoc = None):
    return property(**locals())

class c_int_p(ctypes.POINTER(ctypes.c_int)):
    pass

def c_int_array_p(c_int_array):
    return c_int_array.ctypes.data_as(c_int_p)

class List(ctypes.Structure):
    # For use with _ListFirst and _ListNext
    pass

List._fields_ = [
    ("next", ctypes.POINTER(ctypes.c_int)),
    ("data", ctypes.c_int),
]

Int_p = ctypes.POINTER(ctypes.c_int)

class List2(ctypes.Structure):
    # For use with _ListFirst_int_struct and _ListNext_int_struct
    pass

