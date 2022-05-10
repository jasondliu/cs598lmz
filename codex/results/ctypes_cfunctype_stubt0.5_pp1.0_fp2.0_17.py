import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()
</code>
This works for Python 3.4.3, but not for Python 3.5.0. For 3.5.0, I get the error:
<code>TypeError: don't know how to convert parameter 1
</code>
The same error is generated if I use <code>ctypes.c_char_p</code> instead of <code>ctypes.py_object</code>.
How do I do this in Python 3.5.0?


A:

<code>ctypes.py_object</code> is not defined in Python 3.5.0. It is an alias for <code>ctypes.c_void_p</code>.
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; ctypes.py_object
&lt;class 'ctypes.c_void_p'&gt;
</code>

