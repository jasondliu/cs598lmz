import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0
</code>
However, when I try to allocate and use the function like this:
<code>codeptr = m.codealloc(fun)
rval = m.codecall(codeptr)
</code>
I get this error:
<code>ctypes.ArgumentError: argument 1: &lt;class 'OverflowError'&gt;: int too long to convert
</code>
When I remove the return statement from <code>fun()</code>, I get a segmentation fault.
How can I call a Python function from my C module?


A:

The ctypes documentation shows how to define function signatures and how to use a function pointer, but it doesn't show how to create a function pointer from a Python function.  There is a recipe that uses <code>ctypes</code> to subclass Python's <code>PyCObject</code> so that you can instantiate it yourself, but this solution would require some C programming to integrate into a C module.
I prefer the solution provided by Dr. Chuck's blog: Use a Python class as a trampoline by subclassing <code>ctypes.CF
