import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_int)
def my_callback(i):
    print("callback", i)
    return True

f1 = FUNTYPE(my_callback)
f2 = FUNTYPE(my_callback)
print(f1 == f2)
</code>
This prints <code>False</code> on my machine.

