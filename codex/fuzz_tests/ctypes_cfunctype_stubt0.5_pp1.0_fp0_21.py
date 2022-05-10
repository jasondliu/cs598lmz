import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return (1, 2)

class MyClass(ctypes.Structure):
    _fields_ = [('fun', FUNTYPE)]
</code>
The above code works fine, but when I add <code>@ctypes.pythonapi</code> to <code>fun</code>, it will raise an error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "&lt;stdin&gt;", line 6, in fun
TypeError: Don't know how to convert parameter 1
</code>
Why?

