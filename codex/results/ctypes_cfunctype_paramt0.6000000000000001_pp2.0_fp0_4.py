import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

def f(msg):
    print("f:", msg.decode("utf8"))
    return len(msg)

CALLBACK = FUNTYPE(f)

dll.foo(CALLBACK)
</code>

