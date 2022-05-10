import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(n):
    print('myfunc({}) called'.format(n))
    return n * 2

cfunc = FUNTYPE(myfunc)
print(cfunc(42))
</code>
This works. But what if I want to pass a function that takes a <code>float</code> argument?
<code>def myfunc(n):
    print('myfunc({}) called'.format(n))
    return n * 2

cfunc = FUNTYPE(myfunc)
print(cfunc(42.0))
</code>
This fails with:
<code>TypeError: &lt;built-in function myfunc&gt;: Don't know how to convert parameter 1
</code>
I can't find a way to specify the argument type in the <code>FUNTYPE</code> call.
How can I pass a function with a <code>float</code> argument to <code>ctypes</code>?


A:

You can use <code>ctypes.c_float</code> to
