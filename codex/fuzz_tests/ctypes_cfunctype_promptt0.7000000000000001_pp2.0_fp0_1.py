import ctypes
# Test ctypes.CFUNCTYPE
__doc__ = """
>>> add1 = lambda n: n+1
>>> add1.__name__
'<lambda>'
>>> add1.__module__
'<string>'

>>> def add1(n): return n+1
>>> add1.__name__
'add1'
>>> add1.__module__
'<string>'

>>> f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(add1)
>>> f.__name__
'<lambda>'
>>> f.__module__
'<string>'

>>> def add1(n): return n+1
>>> f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(add1)
>>> f.__name__
'add1'
>>> f.__module__
'<string>'

>>> f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda n: n+1)
>>> f.__name__
'<
