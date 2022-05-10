import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.py_object, ctypes.py_object)
class light_key_s(ctypes.Structure):
    _fields_ = [('name', ctypes.c_char_p),
                ('func', FUNTYPE)]

class light_key_s_array(ctypes.Structure):
    _fields_ = [('data', ctypes.POINTER(light_key_s)),
                ('size', ctypes.c_int),
                ('capacity', ctypes.c_int)]

class light_func_s(ctypes.Structure):
    _fields_ = [('name', ctypes.c_char_p),
                ('code', ctypes.c_char_p),
                ('f', ctypes.py_object),
                ('keys', light_key_s_array)]

class light_func_s_array(ctypes.Structure):
    _fields_ = [('data', ctypes.POINTER(light_func_s)),
                ('size', ctypes.c_int),
                ('capacity', ctypes.c_int
