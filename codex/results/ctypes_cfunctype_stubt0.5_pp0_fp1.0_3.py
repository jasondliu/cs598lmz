import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
And you get:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    print fun()
ctypes.ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: Don't know how to convert parameter 1
</code>
So how can I get the return value?


A:

You need to specify the return type of your function.
The <code>CFUNCTYPE</code> constructor takes the type of the return value as the first argument, and the types of the arguments as the following arguments.
Since you don't have any arguments, you can use <code>None</code> instead of an empty tuple.
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, None)
</code>

