import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
And, I got the following error from the above code.
<code>$ python3 test.py 
Traceback (most recent call last):
  File "test.py", line 5, in &lt;module&gt;
    print(fun())
SystemError: &lt;built-in function fun&gt; returned a result with an error set
</code>
How can I fix the above error?


A:

The problem here is that you're returning a Python string from a C function. That's not allowed, because CPython's C API doesn't have a way to specify the type of the return value. In particular, it doesn't have a way to specify that the return value is a Python object, so the interpreter has no way to know that it needs to increment the reference count on the object.
The easiest thing to do is to return an integer. That's not very useful, but it proves that the problem is with returning the Python object, not with calling the C function.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ct
