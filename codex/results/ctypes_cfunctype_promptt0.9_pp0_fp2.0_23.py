import ctypes
# Test ctypes.CFUNCTYPE()

@returns(ctypes.c_int64)
@argtypes(ctypes.c_int64, ctypes.c_int32)
def _fibonacci_int_callback(start, length):
    """Do the heavy lifting of calculating a series of fibonacci numbers.
    """
    if not isinstance(length, int):
        raise ValueError("Can't calculate fibonacci numbers for non-integer lengths.")

    result = ctypes.c_int64()
    for i in range(length):
        if i == 0: result.value = start
        elif i == 1: result.value = start + 1
        else: result.value = result.value + last_result.value
        last_result = result
    return result.value

lib.fibonacci_int_callback.restype = None
lib.fibonacci_int_callback.argtypes = [ctypes.c_int32, ctypes.CFUNCTYPE(ctypes.c_int64, ctypes.c_int64, ctypes.c_int32)]

