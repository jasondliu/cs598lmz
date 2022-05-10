import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_function(func):
    return FUNTYPE(func)

def make_struct(fields):
    class Struct(ctypes.Structure):
        _fields_ = fields
    return Struct

def make_struct_array(struct, size):
    return (struct * size)()

def make_array(size):
    return (ctypes.c_double * size)()

def make_array_from_list(list):
    return (ctypes.c_double * len(list))(*list)

def make_matrix(n, m):
    return (ctypes.c_double * n * m)()

def make_matrix_from_list(list):
    n = len(list)
    m = len(list[0])
    return (ctypes.c_double * n * m)(*[item for sublist in list for item in sublist])

def make_pointer(value):
    return ctypes.pointer(value)

def make_pointer_to_
