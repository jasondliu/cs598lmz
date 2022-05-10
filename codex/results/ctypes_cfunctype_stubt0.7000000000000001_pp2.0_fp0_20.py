import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Printing from C")
print(type(fun)) # <class 'ctypes.CFUNCTYPE'>
print(fun) # &lt;ctypes.CFUNCTYPE object at 0x7f6fceda0728&gt;
print(fun()) # Printing from C
# &lt;class 'ctypes.PyCFuncPtrType'&gt;
</code>


A:

The <code>CFUNCTYPE</code> class is callable and returns a function pointer.
From the documentation:
<blockquote>
<p>This function can be used to create C callable function pointers from Python callables. The returned object must be called with exactly the specified argument types and will return the specified result type.</p>
</blockquote>

