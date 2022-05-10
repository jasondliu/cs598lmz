import ctypes
# Test ctypes.CField
assert isinstance(ctypes.CField, type)
assert issubclass(ctypes.CField, object)
assert hasattr(ctypes.CField, "__new__")
assert hasattr(ctypes.CField, "__init__")
assert hasattr(ctypes.CField, "__del__")
assert hasattr(ctypes.CField, "__get__")
assert hasattr(ctypes.CField, "__set__")
assert hasattr(ctypes.CField, "from_address")
assert hasattr(ctypes.CField, "offset")
assert hasattr(ctypes.CField, "size")
assert hasattr(ctypes.CField, "pack_into")
assert hasattr(ctypes.CField, "unpack_from")
