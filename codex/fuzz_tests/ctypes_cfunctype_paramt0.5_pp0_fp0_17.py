import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(a):
    return a

cfunc = FUNTYPE(myfunc)

print cfunc(10)
</code>
But I get the error:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    cfunc = FUNTYPE(myfunc)
TypeError: expected CFUNCTYPE instance, got function
</code>
What am I doing wrong?


A:

The documentation for <code>ctypes.CFUNCTYPE</code> says:
<blockquote>
<p>The function must return an integer or a ctypes instance, or it must raise an exception. </p>
</blockquote>
Your function doesn't return an integer and it doesn't return a ctypes instance, so the call to <code>CFUNCTYPE</code> fails with a <code>TypeError</code>.
If you want to create a callback function that returns a Python integer, you should use <code>ctypes.PY
