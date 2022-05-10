import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    print fun()
TypeError: 'PyCFunction' object is not callable
</code>
I'm using Python 2.7.3 on Windows 7.


A:

You need to call <code>fun.restype</code> to set the return type of the function.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun.restype = ctypes.py_object
print fun()
</code>

