import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Printing from C")
print(type(fun)) # <class 'ctypes.CFUNCTYPE'>
print(fun) # &lt;ctypes.CFUNCTYPE object at 0x7f6fceda0728&gt;
print(fun()) # Printing from C
# &lt;class 'ctypes.PyCFuncPtrType'&gt;
