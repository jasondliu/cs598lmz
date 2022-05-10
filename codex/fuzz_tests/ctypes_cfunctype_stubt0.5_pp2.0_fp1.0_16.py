import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hi'

print(fun())
</code>
The error is the following:
<code>Traceback (most recent call last):
  File "./test.py", line 6, in &lt;module&gt;
    print(fun())
  File "/usr/lib64/python3.7/ctypes/__init__.py", line 373, in __call__
    return self._function(*args)
TypeError: 'bytes' object is not callable
</code>


A:

The problem is that you're trying to call a <code>bytes</code> object.
<code>fun</code> is a <code>ctypes.CFUNCTYPE</code> object, which has a <code>__call__</code> method.  But when you print it, you're getting the result of calling <code>fun.__call__</code>, which is the same as calling <code>fun</code> directly.  That returns a <code>bytes</code> object, which is a series of bytes representing the contents of the function.  You can't call a <code
