import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

fun()
</code>
This gives me the error:
<code>Traceback (most recent call last):
  File "test.py", line 71, in &lt;module&gt;
    fun()
TypeError: 'CFUNCTYPE' object is not callable
</code>
I am using Python 2.7.9.


A:

<code>CFUNCTYPE</code> is a type, not a function. Use <code>CFUNCTYPE(ctypes.py_object)(fun)</code> to create a callable object.

