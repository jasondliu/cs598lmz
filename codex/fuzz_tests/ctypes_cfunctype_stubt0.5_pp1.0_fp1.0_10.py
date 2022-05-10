import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello world"
print fun()
</code>
The above code works fine, but I am not sure if it is safe to use it. Is it safe?


A:

Yes, it is safe.
If you want to see what is going on, try this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello world"
print fun.__call__.__code__.co_consts
</code>
You will get:
<code>(None, 'Hello world')
</code>
As you can see, the return value is stored in the <code>co_consts</code> tuple of the code object.

