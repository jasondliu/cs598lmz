import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)

def func(x):
    return x**2

f = FUNTYPE(func)

f(1.0)
</code>
I am trying to do something similar to this, but with the function I want to pass to <code>f</code> being a function that takes a <code>numpy</code> array as input. When I have tried this, I have gotten an error:
<code>def func(x):
    return np.sum(x**2)

f = FUNTYPE(func)
</code>
<blockquote>
<p>ValueError: Procedure called with not enough arguments (4 bytes missing) or wrong calling convention</p>
</blockquote>
How do I fix this error?


A:

The problem is that the C function expects a double input and you're passing it a numpy array.
According to the error message, the function expects a double pointer (you can tell this because the error message is saying that it's missing 4 bytes of input as opposed to 1 byte).
As I understand it, this means that
