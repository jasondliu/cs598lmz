import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)

def call_c_function(function_name, *args):
    py_function = ctypes.pythonapi.PyObject_GetAttrString
    py_function.restype = ctypes.py_object
    py_function.argtypes = (ctypes.py_object, ctypes.c_char_p)
    return_value = py_function(ctypes.py_object(function_name), ctypes.c_char_p(b'__call__'))(args)
    return return_value

# convert the input to a string representation that can be processed by matlab
def matrix_string(input_value):
    return "\n".join(["".join([str(l) for l in list(t)]) for t in list(input_value)])
def vector_string(input_value):
    """ convert vector to string representation for matlab """
    return "".join([str(l) for l in list(input_value)])

def add_noise_layer(input_matrix,
