import ctypes
# Test ctypes.CFUNCTYPE
def func_c_type(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

f = ctypes.CFUNCTYPE(None, ctypes.py_object, ctypes.c_float, ctypes.c_char_p)(func_c_type)

# Test with arg type list
f(1, 2.5, b"hello")
f([1,2,3], 2.5, b"hello")
f((1,2,3), 2.5, b"hello")
# Test with arg type list and arg type conversion
f(b"hello", 2.5, b"hello")
f(b"hello", 2.5, b"hello", convert_c_float=True)
