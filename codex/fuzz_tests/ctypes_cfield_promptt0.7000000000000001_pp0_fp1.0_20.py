import ctypes
# Test ctypes.CField
assert(ctypes.CField.__mro__ == (ctypes.CField, object))
assert(ctypes.CField.from_address.__class__ == types.BuiltinMethodType)
assert(ctypes.CField.from_param.__class__ == types.BuiltinMethodType)

# Test ctypes.Array
assert(ctypes.Array.__mro__ == (ctypes.Array, object))
assert(ctypes.Array._length_ == 2)
assert(ctypes.Array._type_ == ctypes.POINTER(ctypes.c_int))

# Test ctypes.Union
assert(ctypes.Union.__mro__ == (ctypes.Union, object))
assert(ctypes.Union._fields_ == [])

# Test ctypes.Structure
assert(ctypes.Structure.__mro__ == (ctypes.Structure, object))
assert(ctypes.Structure._fields_ == [])

# Test ctypes.POINTER
assert(ctypes.POINTER.__mro__ == (ctypes.POINTER, object
