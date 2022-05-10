import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())
</code>
But this fails with
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    print(fun())
TypeError: 'int' object is not callable
</code>
The question is, is there a way to make this work?


A:

You can use <code>ctypes.pythonapi.PyInt_FromLong</code> to create a PyObject* from an int.
<code>import ctypes

PyInt_FromLong = ctypes.pythonapi.PyInt_FromLong
PyInt_FromLong.restype = ctypes.py_object

FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return PyInt_FromLong(42)

print(fun())
</code>

