import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_char_p)
@FUNTYPE
def fun(x, n, name):
    print(x[0])
    print(n)
    print(name)
    return 42

# And here's how we use it:
fun(array_1d_double(5),5,b"example_name")
</code>

