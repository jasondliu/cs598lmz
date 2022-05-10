import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    return x + 1

f = FUNTYPE(myfunc)
print f(1)
</code>
This works fine, but I want to be able to pass a function that takes more than one argument.  I tried this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(x, y):
    return x + y

f = FUNTYPE(myfunc)
print f(1, 2)
</code>
But I get the error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    f = FUNTYPE(myfunc)
TypeError: expected LP_CFUNCTYPE instance, got function
</code>
I've tried a few other things, but I can't figure out how to do this.  I'm sure it's possible, but I can't
