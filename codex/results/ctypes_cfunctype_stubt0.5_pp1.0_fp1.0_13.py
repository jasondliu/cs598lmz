import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

print fun()
</code>
Gives the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python2.7/ctypes/__init__.py", line 358, in __call__
    return self._internal_func(*args)
TypeError: in method 'fun', argument 1 of type 'PyObject *'
</code>
I don't understand why I am getting this error.  My understanding is that <code>ctypes.py_object</code> is the C equivalent of <code>PyObject *</code>.  So why is it complaining about the argument type?
I am using Python 2.7.3 on Ubuntu 12.04


A:

The problem is that you're trying to call the <code>fun</code> function from Python.  You can't do that, because it's a C function, not a Python function.  To call it from Python, you need to wrap it in a Python function.  For example:

