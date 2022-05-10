import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 5
</code>
This fails with a <code>ValueError</code> exception:
<code>ValueError: CFUNCTYPE(c_void_p)(&lt;function fun at 0x7f6dff764f50&gt;) did not create an executable function
</code>
Reading the docs, I thought <code>py_object</code> was the correct return type.  It's the closest thing to Python's <code>object</code> type.  I'm running on a 64-bit Ubuntu machine, and the documentation for <code>py_object</code> says:
<blockquote>
<p>A Python object. This is the same as c_void_p. However, ctypes does not interpret the value as a pointer, so c_void_p is usable for all pointers and c_py_object is only usable for Python objects.</p>
</blockquote>
So what am I doing wrong?


A:

You are doing almost nothing wrong.  You are using the wrong sample code.  It works fine when you change the placeholder function to return an integer.
<code
