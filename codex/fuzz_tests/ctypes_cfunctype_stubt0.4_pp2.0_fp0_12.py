import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

# This is a Python 2/3 compatible way to get a C string
def to_cstr(s):
    if isinstance(s, bytes):
        return s
    else:
        return s.encode('utf-8')

# This is a Python 2/3 compatible way to get a C string
def from_cstr(s):
    if isinstance(s, bytes):
        return s.decode('utf-8')
    else:
        return s

# This is a Python 2/3 compatible way to get a C string
def to_cstr(s):
    if isinstance(s, bytes):
        return s
    else:
        return s.encode('utf-8')

# This is a Python 2/3 compatible way to get a C string
def from_cstr(s):
    if isinstance(s, bytes):
        return s.decode('utf-8')
    else:
        return s

# This is a Python 2/3 compatible way to get a C string
def to_cstr(s):
