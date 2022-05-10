import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

cpp_lib.cpp_function(fun)

cpp_lib.call_py_function()

&gt;&gt;&gt; hello world
</code>

