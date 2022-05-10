import ctypes
ctypes.cast(0, ctypes.py_object)
&lt;__main__.LP_PyObject object at 0x00000000044B0E20&gt;
</code>
What I do not understand is that, when I do <code>LP_PyObject(0)</code> in python, I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: __init__() takes exactly 2 arguments (1 given)
</code>
So, what is exactly <code>ctypes.cast(0, ctypes.py_object)</code> doing?


A:

<code>ctypes.cast</code> is the way to cast pointers from one type to another, e.g. to make <code>ctypes.pointer(x)</code> where <code>x</code> is a <code>ctypes</code> object into a <code>ctypes.POINTER(ctypes.c_int)</code>.
<code>LP_PyObject</code> is a <
