import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
fun()
</code>
But this gives me the following error:
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    fun()
ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: Don't know how to convert parameter 1
</code>
I have also tried <code>ctypes.CFUNCTYPE(ctypes.c_void_p)</code> but this gives me the same error.
I am using Python 3.6.2.

