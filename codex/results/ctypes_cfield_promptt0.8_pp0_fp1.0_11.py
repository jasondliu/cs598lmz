import ctypes
# Test ctypes.CField
assert issubclass(ctypes.CField, object)
assert not issubclass(ctypes.CField, list)
assert not issubclass(ctypes.CField, ctypes.CField)
assert not issubclass(ctypes.CField, ctypes.Structure)

# Test ctypes.Field
assert issubclass(ctypes.Field, object)
assert not issubclass(ctypes.Field, list)
assert not issubclass(ctypes.Field, ctypes.CField)

# Test ctypes.Union
assert issubclass(ctypes.Union, object)
assert not issubclass(ctypes.Union, ctypes.CField)
assert issubclass(ctypes.Union, ctypes.Structure)

# Test ctypes.Structure
assert issubclass(ctypes.Structure, object)
assert not issubclass(ctypes.Structure, list)
assert not issubclass(ctypes.Structure, ctypes.CField)

# Test ctypes.Array
assert issubclass(ctypes.Array, object)
assert
