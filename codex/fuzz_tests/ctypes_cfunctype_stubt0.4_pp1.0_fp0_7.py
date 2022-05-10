import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
This works fine, but when I try to pass a function as an argument to another function, I get a <code>TypeError</code> exception:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def fun2(f):
    return f()

print fun2(fun)
</code>
Error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    print fun2(fun)
  File "test.py", line 5, in fun2
    return f()
TypeError: 'CFUNCTYPE' object is not callable
</code>
Why is this happening?


A:

It's because the <code>@FUNTYPE</code> decorator doesn't return a callable function; it returns a <code>CFUNCTYPE</code> object.
You can make it work by calling <
