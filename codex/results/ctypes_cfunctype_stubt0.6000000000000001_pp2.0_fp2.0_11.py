import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0
</code>
This works in Python 2.7 but fails in Python 3.6 with the error message:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: must be convertible to a pointer
</code>
What is the correct way to create a CFUNCTYPE in Python 3?


A:

The problem was that the <code>ctypes</code> module has been split into two in Python 3.6. The <code>ctypes</code> module does not contain the <code>CFUNCTYPE</code> constructor anymore. Instead, it is defined in the <code>_ctypes</code> module.
So the solution is to replace <code>ctypes.CFUNCTYPE</code> by <code>ctypes._CFUNCTYPE</code>:
<code>import ctypes
FUNTYPE = ctypes._CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0
</code>

