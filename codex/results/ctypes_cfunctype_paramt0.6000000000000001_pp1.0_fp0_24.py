import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def f(x):
    pass

func = FUNTYPE(f)
func()
</code>
It gives an error:
<code>TypeError: expected integer, got NoneType
</code>
But if I replace <code>f</code> with the following function:
<code>def f(x):
    return x
</code>
It works.
I thought it was because I was returning <code>None</code>, but it seems not. What is the issue?


A:

The issue is that you're declaring a function that returns <code>None</code> but then calling it with a type that returns <code>void</code>. It's like if you declared a function in C that returns an <code>int</code> but then called it with a type that returns <code>void</code>.

