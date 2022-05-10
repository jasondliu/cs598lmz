import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def f(x):
    return x + 1

cfunc = FUNTYPE(f)
print cfunc(1)
</code>
This code works fine, but I want to use a function that takes a pointer to a function as argument.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def f(x):
    return x + 1

cfunc = FUNTYPE(f)

def g(f):
    return f(1)

print g(cfunc)
</code>
This code fails with the following error:
<code>Traceback (most recent call last):
  File "test.py", line 13, in &lt;module&gt;
    print g(cfunc)
TypeError: argument must be callable
</code>
How can I pass <code>cfunc</code> to <code>g</code>?


A:

You can't pass a function pointer to a Python function
