import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
This gives me the following error:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    print fun()
TypeError: 'PyCFunctionObject' object is not callable
</code>
I am using Python 2.7.3.
Any help would be appreciated.


A:

You need to call <code>fun.restype = ctypes.py_object</code> before calling <code>fun</code>.

