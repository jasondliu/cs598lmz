import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

sys.create_dynamic_module("&lt;test&gt;", f"import re, sys; sys.modules['&lt;test&gt;'].__dict__.update(fun=fun()); sys.modules['&lt;test&gt;'].__dict__.update(__file__='C:\\\\Path\\\\To\\\\This\\\\Py\\\\File')")
</code>
so all it does is try to import, and then inject the module with a function, but it fails to get even an import statement, reaping an import error "No module named '_bootstrap'"


A:

You can check for the code object of the function
<code>&gt;&gt;&gt; def foo():
    pass

&gt;&gt;&gt; foo.__code__.co_code
b'd\x05}K\x01\x00S'
</code>
This has to be <code>str</code> would be the class of the function object.

