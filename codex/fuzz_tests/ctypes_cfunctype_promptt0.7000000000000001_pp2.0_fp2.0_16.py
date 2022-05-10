import ctypes
# Test ctypes.CFUNCTYPE
X = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
X.__name__ = 'X'
try:
    X.__qualname__ = 'X'
except AttributeError:
    pass
F = X(lambda x, y: x + y)
assert F(1, 2) == 3
assert F.__name__ == 'X'
try:
    assert F.__qualname__ == 'X'
except AttributeError:
    pass
assert F.__code__.co_argcount == 2
assert F.__code__.co_varnames == ('x', 'y')
X = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
X.__name__ = 'X'
try:
    X.__qualname__ = 'X'
except AttributeError:
    pass
F = X(lambda x: lambda y: x + y)
assert F(2)(3) == 5
assert
