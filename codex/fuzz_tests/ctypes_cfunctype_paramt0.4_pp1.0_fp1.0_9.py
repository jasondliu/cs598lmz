import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def py_func(x):
    return x + 1

c_func = FUNTYPE(py_func)

print c_func(2)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    c_func = FUNTYPE(py_func)
  File "/usr/lib/python2.7/ctypes/__init__.py", line 361, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: /tmp/test.so: undefined symbol: PyCFunction_Type
</code>
Why is this happening? How can I fix it?


A:

You can't.  The Python interpreter is written in C.  The <code>PyCFunction_Type</code> symbol is defined in the Python interpreter, not in the Python standard library.

