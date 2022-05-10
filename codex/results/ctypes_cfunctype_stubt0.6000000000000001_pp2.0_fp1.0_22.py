import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
</code>
or
<code>def fun():
    return None

FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)(fun)
</code>
But I got an error:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)(fun)
TypeError: must be convertible to a pointer
</code>
I don't know how to fix it. Any help would be appreciated!


A:

You can't use <code>CFUNCTYPE</code> to wrap a function that returns <code>None</code> or <code>void</code>.  <code>ctypes</code> doesn't know what to pass to the function as an <code>argtypes</code> argument, and you can't pass <code>None</code> because that's the default for <code>argtypes</code>.  The <code>CFUNCTYPE</code> constructor takes an <code
