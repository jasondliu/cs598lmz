import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double

class A(ctypes.Structure):
    '''
    >>> s = S()
    >>> s.x = 3.0
    >>> s.y = 4.0
    >>> a = A()
    >>> a.s = s
    >>> a.s.x
    3.0
    >>> a.s.y
    4.0
    '''
    _fields_ = [("s", S)]

class B(ctypes.Structure):
    _fields_ = [("s", S), ("d", ctypes.c_double)]

class C(ctypes.Structure):
    _fields_ = [("s", S), ("a", A)]

class D(ctypes.Structure):
    _fields_ = [("s", S), ("b", B)]

class E(ctypes.Structure):
    _fields_ = [("s", S), ("c", C)]

if __name__ == "__main__":
    import doctest
    doctest.test
