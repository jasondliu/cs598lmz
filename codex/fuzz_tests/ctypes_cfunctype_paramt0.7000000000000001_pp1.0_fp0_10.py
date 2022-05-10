import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
def _wrap(func):
    FUN = FUNTYPE(func)
    FUN.restype = ctypes.c_void_p
    return FUN

def _tostring(value):
    size = value.c_len
    string = ctypes.string_at(value.c_ptr, size)
    string = string.decode('utf-8')
    return string

def _cstring(value):
    string = value.encode('utf-8')
    return ctypes.create_string_buffer(string)

def _ctype(value):
    return ctypes.c_void_p(value)

def _toarray(array, type):
    length = array.c_len
    result = (type * length)()
    for i in range(length):
        result[i] = array.c_ptr[i]
    return result

def _array(array, type):
    length = len(array)
    result = (type * length)(*array)
    return ctypes.cast
