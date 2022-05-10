import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_function(func):
    return FUNTYPE(func)

def make_callback(func):
    return FUNTYPE(func)

def make_value(func):
    return FUNTYPE(func)

def make_vector(func):
    return FUNTYPE(func)

def make_matrix(func):
    return FUNTYPE(func)

def make_matrix_vector(func):
    return FUNTYPE(func)

def make_vector_matrix(func):
    return FUNTYPE(func)

def make_matrix_matrix(func):
    return FUNTYPE(func)

def make_matrix_matrix_matrix(func):
    return FUNTYPE(func)

def make_matrix_matrix_vector(func):
    return FUNTYPE(func)

def make_matrix_vector_matrix(func):
    return FUNTYPE(func)

def make_vector_matrix_matrix(func):
    return FUNTYPE(func)

