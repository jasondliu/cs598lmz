import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
</code>
And then I would like to call the following function:
<code>def f(x, y):
    return x + y
</code>
But the following code will not work:
<code>val = S()
val.x = 10
val.y = 20
f(val.x, val.y)
</code>
because C types are not Python types.
So I would like to do the following:
<code>val = S()
val.x = 10
val.y = 20
f(*val)
</code>
I know that I could use <code>ctypes</code>'s <code>byref</code> function to get the address of <code>val</code>, but I would like to know if it is possible to convert the <code>ctypes</code> <code>Structure</code> to a tuple of C types.


A:

You can use <code>tuple(val)</code>.
<code>import ctypes

class S(ctypes.Structure
