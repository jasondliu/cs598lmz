import ctypes
# Test ctypes.CField instance
print(type(ctypes.CFuncPtr.restype))       # => <class 'ctypes.CField'>
print(type(ctypes.CFuncPtr.restype.type))  # => <class 'ctypes.CField'>

# CField has a `type` attribute
c_int_p = ctypes.POINTER(ctypes.c_int)
print(c_int_p.type)  # => <class 'ctypes.ctypes._SimpleCData'>

# but `type` is not a member of its type
print(dir(ctypes.CField))                   # => ['__class__', '__delattr__',
                                            # ... '__slots__']
print('type' in ctypes.CField.__slots__)    # => False
print('type' in dir(ctypes.CField))         # => True
