import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    print(x)
    return x

cfunc = FUNTYPE(func)

print(cfunc(1))
</code>
This works fine and the output is:
<code>1
1
</code>
But if I change the <code>print(x)</code> line to <code>print(x+1)</code>, the output is:
<code>2
2
</code>
The output is the same as if I had not changed the code. It seems that the function is not being called at all.
Is this a bug in Python or am I doing something wrong?


A:

<code>ctypes</code> uses a lot of caching under the hood, so you need to explicitly tell it that the function you are passing in is dynamic.
<code>cfunc = FUNTYPE(func, use_errno=True, use_last_error=True)
</code>

