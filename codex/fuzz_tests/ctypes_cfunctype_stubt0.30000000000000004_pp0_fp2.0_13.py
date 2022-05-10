import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    print(fun())
TypeError: 'str' object is not callable
</code>
I don't understand why it says that <code>str</code> is not callable.
If I change the return type to <code>ctypes.c_char_p</code>, it works.
I'm using Python 3.5.2 on Windows 10.


A:

<code>ctypes.py_object</code> is a type that can hold any Python object.  It's not a type that can be used to return a Python object from a C function.  Use <code>ctypes.c_char_p</code> instead.

