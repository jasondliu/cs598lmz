import ctypes
# Test ctypes.CField.from_address
# Create a class that contains a pointer
class Foo(ctypes.Structure):
    _fields_ = [("ptr", ctypes.POINTER(ctypes.c_int))]

# Create a ctypes instance from raw memory
value = ctypes.c_int(42)
addr = ctypes.addressof(value)
obj = ctypes.CField.from_address(addr, ctypes.POINTER(ctypes.c_int))

# Access members of the returned object
print(obj.contents)
print(obj.contents.value)

# Modify members of the returned object
obj.contents.value += 1
print(obj.contents.value)
print(value.value)

# Test ctypes.CField.from_buffer
# Create a class that contains a pointer
class Bar(ctypes.Structure):
    _fields_ = [("ptr", ctypes.POINTER(ctypes.c_int))]

# Create a ctypes instance from a buffer
value = ctypes.c_int(42)
buf = c
