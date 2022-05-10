import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())
</code>
This works, but only if the function is defined in a module. If I try to do the same in the interactive interpreter, it doesn't work:
<code>&gt;&gt;&gt; from ctypes import *
&gt;&gt;&gt; FUNTYPE = CFUNCTYPE(py_object)
&gt;&gt;&gt; @FUNTYPE
... def fun():
...     return 42
...
&gt;&gt;&gt; fun()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "&lt;stdin&gt;", line 2, in fun
TypeError: an integer is required
</code>
Is there a way to make this work in the interactive interpreter?
I'm using Python 3.2.2 on Windows.


A:

I think the problem is that the <code>CFUNCTYPE</code> constructor returns a new type object, and the <code>@</code> decor
