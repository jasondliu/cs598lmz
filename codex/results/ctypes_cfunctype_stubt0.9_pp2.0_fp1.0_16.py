import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World!"
</code>
then calling <code>fun()</code> from javascript (with pyodide):
<code>&gt; pyodide.globals.fun()
"Hello World!"
</code>

