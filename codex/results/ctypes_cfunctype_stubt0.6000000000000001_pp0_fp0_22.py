import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

assert fun() == "hello"
</code>
But if I try to do the same thing with a <code>ctypes.c_wchar_p</code> object, it fails:
<code>&gt;&gt;&gt; FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_wchar_p)
&gt;&gt;&gt; @FUNTYPE
... def fun():
...     return "hello"
...
&gt;&gt;&gt; fun()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ValueError: Procedure probably called with not enough arguments (4 bytes missing)
</code>
Why does it work with <code>py_object</code> and not work with <code>c_wchar_p</code>?


A:

<code>ctypes.c_wchar_p</code> is a pointer type.  <code>ctypes.py_object</code> is not.  You can
