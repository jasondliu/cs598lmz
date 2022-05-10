import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

def my_callback(message):
    print "python:", message
    return 0

my_callback = FUNTYPE(my_callback)

lib = ctypes.cdll.LoadLibrary('./cfuncs.so')
lib.call_from_c(my_callback)
</code>
The output is:
<code>python: Hello from C!
</code>

