import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 123
print(fun()) # -&gt; 123
# access the memory address of the funtion (show rawpointer)
print(ctypes.addressof(fun))
# access the content of the function (show tcode)
