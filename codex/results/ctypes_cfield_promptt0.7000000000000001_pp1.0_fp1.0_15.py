import ctypes
# Test ctypes.CField

assert ctypes.sizeof(ctypes.CField) == ctypes.sizeof(ctypes._CField)
assert ctypes.alignment(ctypes.CField) == ctypes.alignment(ctypes._CField)

assert ctypes.CField.__name__ == 'CField'
assert ctypes.CField.__qualname__ == 'CField'
assert ctypes.CField.__module__ == 'ctypes'

# Test ctypes.Field

assert ctypes.sizeof(ctypes.Field) == ctypes.sizeof(ctypes._Field)
assert ctypes.alignment(ctypes.Field) == ctypes.alignment(ctypes._Field)

assert ctypes.Field.__name__ == 'Field'
assert ctypes.Field.__qualname__ == 'Field'
assert ctypes.Field.__module__ == 'ctypes'

# Test ctypes.Union

class TestUnion(ctypes.Union):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c
