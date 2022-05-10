import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
fun()

print(ctypes.cast(fun, ctypes.c_void_p).value)
</code>
From the Python documentation:
<blockquote>
<p>A CFUNCTYPE instance is callable, and creates callable function pointers from Python callables. The callable function pointers are subclasses of _CFuncPtr and can be passed to C functions that expect function pointers as arguments.</p>
</blockquote>

