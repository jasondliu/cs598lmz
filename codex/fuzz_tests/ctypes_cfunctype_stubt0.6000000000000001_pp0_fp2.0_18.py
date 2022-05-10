import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return [1,2,3]

print fun()
</code>
and I get the following error:
<code>RuntimeError: maximum recursion depth exceeded in cmp
</code>
If I change the return type to a <code>ctypes.c_long</code> then it works.
Is this a bug or expected behavior?

