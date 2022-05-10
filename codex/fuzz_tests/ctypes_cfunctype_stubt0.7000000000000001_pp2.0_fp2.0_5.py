import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hi"
</code>
This code creates a callable that returns a string.
However, I would like to make it return a list. So I tried
<code>@FUNTYPE
def fun():
    return ["hi"]
</code>
but that gives me <code>TypeError: must be convertible to a pointer</code>.
I also tried
<code>@FUNTYPE
def fun():
    return ctypes.py_object(["hi"])
</code>
but that gives
<code>TypeError: 'str' does not support the buffer interface</code>
I'm not sure how to do it. Can somebody help?


A:

Just use <code>return ["hi"]</code> as <code>ctypes.py_object</code> is a callable that's used to convert from a Python type to a <code>ctypes</code> type.
<code>In [1]: import ctypes

In [2]: FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

In [3]: @FUNTYPE
   ...: def fun
