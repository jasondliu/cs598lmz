import ctypes
# Test ctypes.CFUNCTYPE
# (e.g. see http://dirtsimple.org/2004/12/python-ctypes-tutorial.html)

int_p = ctypes.POINTER(ctypes.c_int)
#int_p = ctypes.c_void_p

# Callback function.
def print_int(i):
    print i,

def call_print_int(i):
    print_int(i)

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int)
callback = CALLBACK(print_int)

lib = ctypes.CDLL("./libtestcallback.so")
lib.call_callback.argtypes = [CALLBACK, ctypes.c_int]
lib.call_callback(callback, len(sys.argv))
</code>
libtestcallback.c:
<code>#include &lt;stdlib.h&gt;
#include &lt;stdio.h&gt;

typedef void (*print_func)(int);

void call_callback(print_
