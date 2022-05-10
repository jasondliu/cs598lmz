import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(x, y):
    print x+y
    return x+y

lib = ctypes.CDLL('./libfoo.so')
lib.foo.argtypes = [FUNTYPE]
lib.foo(FUNTYPE(callback))
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "./test.py", line 12, in &lt;module&gt;
    lib.foo(FUNTYPE(callback))
TypeError: an integer is required
</code>
I have also tried:
<code>lib.foo(FUNTYPE(callback))
</code>
with the same error.
What am I doing wrong?


A:

You are passing an argument of type <code>ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)</code> to a function that expects an argument of type <code>ctypes.c_int</code>.  You need to pass an argument of type
