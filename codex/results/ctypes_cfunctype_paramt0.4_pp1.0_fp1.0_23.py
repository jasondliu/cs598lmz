import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_double)

def __callback(arg):
    print(arg)

CALLBACK = FUNTYPE(__callback)

lib.set_callback(CALLBACK)

lib.call_callback()
</code>
Output:
<code>1.0
</code>

