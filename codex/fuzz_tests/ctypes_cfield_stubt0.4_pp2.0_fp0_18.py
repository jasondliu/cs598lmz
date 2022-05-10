import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def is_c_field(obj):
    return isinstance(obj, ctypes.CField)

def is_c_struct(obj):
    return isinstance(obj, ctypes.Structure)

def is_c_union(obj):
    return isinstance(obj, ctypes.Union)

def is_c_array(obj):
    return isinstance(obj, ctypes.Array)

def is_c_pointer(obj):
    return isinstance(obj, ctypes.POINTER)

def is_c_function(obj):
    return isinstance(obj, ctypes.CFUNCTYPE)

def is_c_type(obj):
    return isinstance(obj, ctypes._SimpleCData)

def is_c_primitive(obj):
    return isinstance(obj, ctypes._SimpleCData) and not is_c_pointer(obj)

def is_c_string(obj):
    return isinstance(obj, ctypes.c_char_p)

def is_c_void(obj):
   
