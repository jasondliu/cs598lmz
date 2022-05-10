import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def f():
    return "hello"

print fun()
print fun() == f()
print fun() is f()
</code>
This prints:
<code>hello
True
False
</code>
What I don't understand is why <code>fun() is f()</code> is <code>False</code>.
I thought that <code>is</code> tests for object identity.
<code>fun()</code> and <code>f()</code> are both <code>str</code> objects, so why are they not the same object?


A:

<code>is</code> tests for object identity.  <code>fun()</code> and <code>f()</code> are not the same object.
<code>fun()</code> and <code>f()</code> are both <code>str</code> objects, but they are not the same <code>str</code> object.  <code>fun()</code> is a <code>str</code> object created by the C function <code>PyString_FromString
