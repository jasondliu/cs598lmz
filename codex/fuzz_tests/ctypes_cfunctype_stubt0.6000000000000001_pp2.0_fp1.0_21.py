import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 12

print(fun())
</code>
I get the following error:
<code>$ python test.py
Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    print(fun())
TypeError: PyObject_Call() returned a result with an error set
</code>
What is wrong?
Note: I am using Python 2.7.


A:

<code>ctypes.py_object</code> is not a C type, and is not a Python type. It is a special value used by <code>ctypes</code> to return Python objects.
You must return a Python object, such as an int:
<code>@FUNTYPE
def fun():
    return 12
</code>
or a string:
<code>@FUNTYPE
def fun():
    return 'hello'
</code>
or a <code>ctypes</code> object:
<code>@FUNTYPE
def fun():
    return ctypes.c_int(12)
</code>
or something else.

