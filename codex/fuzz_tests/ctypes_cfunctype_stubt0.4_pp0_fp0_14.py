import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 5, in &lt;module&gt;
    print fun()
TypeError: 'PyCFunctionObject' object is not callable
</code>
I have tried to use <code>ctypes.c_char_p</code> instead of <code>ctypes.py_object</code> but I get the same error.


A:

The <code>CFUNCTYPE</code> object is not callable, you need to call the <code>__call__</code> method on it.
<code>print fun.__call__()
</code>

