import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())

# but this will fail
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
<blockquote>
<p>TypeError: cannot create 'function' instances</p>
</blockquote>
I have no idea why this is happening. I am using Python 3.5 on Windows.


A:

You're trying to create a function with the same name as an existing function in the same scope. You can't do that.
If you want to create a different function with the same name, you have to create it in a different scope.
<code>def fun():
    return "hello"

print(fun())

def fun():
    return "goodbye"

print(fun())
</code>

