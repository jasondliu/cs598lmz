import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def f(x, y, z):
    print(x, y, z)

f(S(1, 2, 3))
</code>
This is the error I get:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    f(S(1, 2, 3))
TypeError: f() missing 2 required positional arguments: 'y' and 'z'
</code>
I would expect the output to be <code>1 2 3</code>.
Why does this not work?


A:

<code>S(1, 2, 3)</code> is an instance of <code>S</code>, not a tuple.  You can pass it as a single argument to <code>f</code>, but you need to change <code>f</code> to accept a single argument:
<code>def f(s):
    print(s.x, s.y, s.z
