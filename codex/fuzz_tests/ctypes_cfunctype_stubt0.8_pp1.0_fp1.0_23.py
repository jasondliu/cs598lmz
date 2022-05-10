import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

fun2 = cast(fun, FUNTYPE)
print fun()
print fun2()
print fun == fun2
</code>
So the result is
<code>42
4
False
</code>
In fact the memory of the function object is different, but the function code is the same.
Because <code>__eq__</code> is not implemented in <code>ctypes</code>, I'm not sure how to check if the function code is the same?


A:

One way is to use the Python C API to check if <code>fun</code> and <code>fun2</code> have the same <code>PyCodeObject</code>.
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; import ctypes.util
&gt;&gt;&gt; libpython = ctypes.cdll.LoadLibrary(ctypes.util.find_library("python2.7"))
&gt;&gt;&gt; import sys
&gt;&gt;&gt; libpython.PyFunction_GetCode.rest
