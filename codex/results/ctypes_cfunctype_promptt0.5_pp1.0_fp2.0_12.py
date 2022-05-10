import ctypes
# Test ctypes.CFUNCTYPE, ctypes.c_int, ctypes.c_char_p, ctypes.byref, ctypes.pointer

# Define a callback function
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p)
def py_cmp_func(s1, s2):
    print('py_cmp_func: s1=%s, s2=%s' % (s1, s2))
    return ctypes.c_int(1)

# Register the callback function
lib = ctypes.CDLL('./libclib.so')
cmp_func = CMPFUNC(py_cmp_func)
lib.register_callback(cmp_func)

# Call the C function
lib.call_callback()

# Unregister the callback function
lib.unregister_callback()

# Call the C function again
lib.call_callback()

# Define a structure
class MyStruct(ctypes.Structure):
    _fields_ = [
        ('
