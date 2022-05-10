import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

print fun()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    print fun()
TypeError: 'int' object is not callable
</code>
I am using Python 2.7.3 on Windows 7.
What am I doing wrong?


A:

The problem is that <code>ctypes.py_object</code> is not a valid return type for a <code>CFUNCTYPE</code>. It is only a valid argument type.
The correct way to do this is to use the <code>restype</code> argument to <code>CFUNCTYPE</code>:
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, restype=ctypes.py_object)
</code>

