import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def CField(*args, **kwds):
    return ctypes.CField(*args, **kwds)

def sizeof(tp):
    return ctypes.sizeof(tp)

def itemoffsetof(tp, field):
    return ctypes.offsetof(tp, field)

def itemsof(tp):
    return ctypes.sizeof(tp)

def fieldoffsetof(self, tp, field):
    return getattr(tp, field).offset

def formataddr(addr):
    return repr(addr)

def pyobjectptr(obj):
    return id(obj)

def cast_instance_to_base_ptr(obj):
    # XXX to be implemented
    return obj

def get_array_length(arr):
    return len(arr)

def get_element_address(arr, i):
    return id(arr[i])

def get_function_addr(func):
    return id(func)

def get_function_type(func):
    return type(func)

def get_function_name
