import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def foo(a):
    return a

foo_c = FUNTYPE(foo)

print foo_c(1)
</code>
This prints <code>1</code> as expected. However, if I try to pass a function that takes a <code>float</code> argument, I get an error:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_float)

def foo(a):
    return a

foo_c = FUNTYPE(foo)

print foo_c(1)
</code>
This gives me:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    foo_c = FUNTYPE(foo)
TypeError: cannot be converted to a pointer
</code>
I can't figure out why this is happening.


A:

You're passing a Python function to the <code>CFUNCTYPE</code>
