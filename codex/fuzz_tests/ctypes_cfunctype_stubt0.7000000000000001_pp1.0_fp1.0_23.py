import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    sys.stdout.write('Hello world!')
    return 1

res = fun()
print type(res)
print res

print ctypes.cast(fun, ctypes.c_void_p).value
#print ctypes.cast(fun, ctypes.c_void_p)
</code>
If you want to see a pointer to a function, you need to use <code>ctypes.addressof</code>.  On Windows, this will show you the address of a stub for the function, which loads the DLL and jumps to the real address.
<code>import sys
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    sys.stdout.write('Hello world!')
    return 1

print ctypes.addressof(fun)
</code>

