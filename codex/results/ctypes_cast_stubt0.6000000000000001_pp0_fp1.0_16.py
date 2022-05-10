import ctypes
ctypes.cast(0, ctypes.py_object)

del ctypes

# now the CPython implementation is gone, and the Cython implementation is used
# instead

assert gc.get_count() == (0, 1, 0)

# it should not be possible to create more than one instance

try:
    ctypes.cast(0, ctypes.py_object)
except MemoryError:
    pass
else:
    assert False, "should have raised MemoryError"

try:
    ctypes.cast(0, ctypes.py_object).cast(ctypes.c_int)
except MemoryError:
    pass
else:
    assert False, "should have raised MemoryError"
