import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    # call a function that is defined in C
    return cfun()

print(fun())
#&gt;&gt;&gt; 5
</code>

