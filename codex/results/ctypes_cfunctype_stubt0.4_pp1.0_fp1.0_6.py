import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World"

print fun()
</code>
When I run it, I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    print fun()
ctypes.ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: wrong type
</code>
I am using Python 2.7.3 on Windows 7.
How can I fix this?


A:

The problem is that you are trying to return a Python object from a C function.  That is not allowed.  You can only return an integer, a pointer or a structure.
If you want to return a Python object, you need to use a callback.  In C, you would call the callback with the Python object as the argument.  In Python, you would create a function and pass it to the C function as the callback.
Here is an example:
<code># test.py
import ctypes

# Define a callback type.
CALLBACK_TYPE = ctypes.CFUNCTY
