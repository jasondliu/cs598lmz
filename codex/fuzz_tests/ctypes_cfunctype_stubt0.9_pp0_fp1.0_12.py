import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass
</code>
This gives me an <code>OverflowError</code> when I try to call <code>fun</code>:
<code>fun()
OverflowError: Python int too large to convert to C long
</code>


A:

This feature is currently unimplemented:
<code>&gt;&gt;&gt; def foo():
...     pass
... 
&gt;&gt;&gt; ctypes.CFUNCTYPE(ctypes.py_object)(foo)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
NotImplementedError: function returning py_object
</code>
There  is an open issue for tracking this in the Python bug tracker, see https://bugs.python.org/issue1648806.

