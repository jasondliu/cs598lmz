import ctypes
# Test ctypes.CFUNCTYPE(None, ctypes.c_size_t)*cast(value, _CFUNCTYPE)

def value_pointer(value):
    return (ctypes.CFUNCTYPE(None, ctypes.c_size_t)*cast(value, _CFUNCTYPE))[0]

value_pointer.__doc__ = "value_pointer(value) -> int\nreturns the integer pointer to a value"

def value_integer(value):
    return cast(value_pointer(value), ctypes.c_size_t).value

value_integer.__doc__ = "value_integer(value) -> int\nreturns the integer pointer to a value"

def value_float(value):
    return cast(value_pointer(value), ctypes.c_void_p).value

value_float.__doc__ = "value_float(value) -> float\nreturns the float from a value"

def value_new_integer(other):
    return _value_new_integer(ctypes.c_size_t(other), context.empty())
