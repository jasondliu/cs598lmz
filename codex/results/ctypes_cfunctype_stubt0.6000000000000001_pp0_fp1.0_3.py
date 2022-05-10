import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello, world"

print(fun())
</code>
The above code works fine, but when I try to add a parameter to the function, like this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(a):
    return "hello, world"

print(fun())
</code>
I get an error:
<code>TypeError: Required argument 'a' (pos 1) not found
</code>
What am I missing here?


A:

The problem is that you are using the decorator syntax, which is intended for making the decorated function behave in a certain way, rather than changing its type.
You can either do:
<code>fun = FUNTYPE(fun)
</code>
or
<code>@FUNTYPE
def fun(a):
    return "hello, world"

print(fun(None))
</code>

