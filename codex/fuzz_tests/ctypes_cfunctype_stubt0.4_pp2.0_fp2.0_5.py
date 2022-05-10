import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
print(fun())
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    print(fun())
ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: wrong type
</code>
I am using Python 3.6.3 on Windows 10.
What am I doing wrong?


A:

The problem is that you are trying to return an <code>int</code> from a function that is declared to return a <code>PyObject</code>.  You need to return a <code>PyObject</code> from your function.  You can do this by using the <code>Py_BuildValue</code> function.
<code>from ctypes import *

FUNTYPE = CFUNCTYPE(PyObject)

@FUNTYPE
def fun():
    return Py_BuildValue("i", 1)

print(fun())
</code>

