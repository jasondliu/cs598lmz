import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return(1,2)

print fun() # (1, 2)

# fun() is an object
print(fun)
# &lt;__main__.CFUNCTYPE object at 0x01E9F8B0&gt;

# fun.__call__ is an object
print(fun.__call__)
# &lt;method-wrapper '__call__' of __main__.CFUNCTYPE object at 0x01E9F8B0&gt;

# But when you call fun.__call__, you get the values
# that were returned by the C function.
print(fun.__call__())
# (1, 2)
</code>

