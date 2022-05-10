import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
This works fine, but I'm not sure how to pass arguments to the function.  I tried this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(arg):
    return arg

print fun("hello")
</code>
But this gives me an error:
<code>Traceback (most recent call last):
  File "test.py", line 5, in &lt;module&gt;
    print fun("hello")
TypeError: &lt;built-in function fun&gt; returned a result with an error set
</code>
I'm not sure what I'm doing wrong.  Any help would be appreciated.


A:

The problem is that you're trying to pass a Python object to a C function.  You need to convert the Python object to a C object first.  The easiest way to do this is to use <code>ctypes.py_object</code> as the argument type.  This will automatically
