import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int
)

def function(a, b, c, d):
    print(a, b, c, d)

# ctypes.cast()
# https://docs.python.org/3/library/ctypes.html?highlight=ctypes#ctypes.cast
callb = FUNTYPE(function)

# Create C instance
lib = ctypes.CDLL(
    os.path.join(os.path.dirname(__file__), 'lib.so')
)
lib.C.argtypes = [FUNTYPE, ctypes.c_int]
lib.C.restype = ctypes.c_int
c_obj = lib.C(callb, 100)

# Create Python instance
py_obj = foo.Bar.from_c_object(c_obj)

# Free C instance
lib.free(c_obj)
</code>
<code>// lib.c
#include &
