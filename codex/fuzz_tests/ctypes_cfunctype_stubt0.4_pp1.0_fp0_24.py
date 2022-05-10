import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
The above code does not work. It gives the following error:
<code>Traceback (most recent call last):
  File "C:\Users\Admin\Desktop\test.py", line 6, in &lt;module&gt;
    print(fun())
ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: wrong type
</code>
How can I make this work?


A:

You can't use <code>ctypes.py_object</code> to return a Python object from a C function.
<code>ctypes.py_object</code> is only used to pass Python objects to C functions. It is a wrapper around <code>PyObject*</code> that handles reference counting.
You can return a <code>PyObject*</code> directly from a C function, but you must increment the reference count of the object before returning it.
<code>Py_RETURN_OBJECT</code> is a macro that increments the reference count of the object it is given, and returns it.

