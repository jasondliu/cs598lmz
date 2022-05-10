import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"
print fun.__module__
print fun()
</code>
The output:
<code>ctypes
fun
</code>
Is there any means to make the output <code>__main__</code> instead of <code>ctypes</code>?


A:

Are you expecting the fun object to be callable, or are you wanting to override the module name of the function? 
As you've written it, the function object is callable, so it can be used in the same way that a function is used. It just has a different module name. 

