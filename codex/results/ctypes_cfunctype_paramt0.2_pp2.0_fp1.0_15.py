import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(x, y):
    print("my_callback called with %d, %d" % (x, y))
    return x + y

my_callback_c = FUNTYPE(my_callback)

# This is the function we want to call from C.
def my_function(x, y, callback):
    print("my_function called with %d, %d" % (x, y))
    return callback(x, y)

my_function_c = FUNTYPE(my_function)

# This is the C code we want to compile.
CODE = """
int my_function_c(int x, int y, int (*callback)(int, int)) {
    printf("my_function_c called with %d, %d\\n", x, y);
    return callback(x, y);
}
"""

# Compile the C code into a shared library.
import tempfile
import os

with tempfile.NamedTemporaryFile(suff
