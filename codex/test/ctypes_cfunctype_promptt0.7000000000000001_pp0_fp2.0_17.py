import ctypes
# Test ctypes.CFUNCTYPE

prototype = ctypes.CFUNCTYPE(None)
impl = prototype(lambda: None)
print(impl)
impl()

print(type(impl))
