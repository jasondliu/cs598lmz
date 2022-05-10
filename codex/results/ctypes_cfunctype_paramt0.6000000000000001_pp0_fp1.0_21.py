import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def mycallback(arg):
    print("mycallback called with arg:", arg)
    return 0

lib = ctypes.CDLL("./mylib.so")
mycallback_c = FUNTYPE(mycallback)
lib.set_callback(mycallback_c)
lib.call_callback(2)
</code>
Compile the C program with:
<code>gcc -shared -o mylib.so -fPIC mylib.c
</code>

