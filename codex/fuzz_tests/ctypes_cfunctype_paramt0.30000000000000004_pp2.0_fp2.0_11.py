import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(a):
    print a
    return a

f = FUNTYPE(myfunc)
f(2)
</code>
This works as expected.  Now I want to use a function that takes a double as an argument:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)

def myfunc(a):
    print a
    return a

f = FUNTYPE(myfunc)
f(2)
</code>
This fails with the error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    f(2)
ctypes.ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: wrong type
</code>
Why does this fail?  How can I make it work?


A:

<code>ctypes.c_double</code> is not a Python float,
