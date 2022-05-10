import ctypes
ctypes.cast(None, ctypes.c_void_p).value

# AttributeError: 'NoneType' object has no attribute 'value'

