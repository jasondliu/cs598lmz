import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 5, in &lt;module&gt;
    print(fun())
TypeError: 'PyCFunction' object is not callable
</code>
I have tried to find the answer to this question, but I have not been able to find it.
I am using Python 3.6.1.


A:

You need to use <code>ctypes.pythonapi</code> to get the Python C API.
<code>import ctypes

PyCFunction = ctypes.pythonapi.PyCFunction_Type
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>

