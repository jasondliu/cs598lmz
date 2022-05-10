import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

my_lib = ctypes.CDLL('/usr/lib/libc.dylib')

my_lib.my_func.restype = ctypes.c_int
my_lib.my_func.argtypes = [ctypes.c_int]

class PyClass(object):
    def __init__(self, my_int):
        self.my_int = my_int

    def my_method(self, x):
        return my_lib.my_func(x)

def my_callback(x):
    return my_lib.my_func(x)

my_callback_func = FUNTYPE(my_callback)

my_lib.set_callback(my_callback_func)

my_class = PyClass(123)

print my_class.my_method(123)
</code>
And here is my <code>my_lib.c</code> file:
<code>#include &lt;stdio.h&gt;
#include &lt;stdlib.
