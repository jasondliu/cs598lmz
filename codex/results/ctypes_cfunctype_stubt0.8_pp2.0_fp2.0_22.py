import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    yield 1
    return
    yield 2
</code>
which results in a <code>TypeError</code>:
<code>TypeError: generator cannot do non-object yield
</code>
But if I use a regular function, instead of a generator, it works:
<code>@FUNTYPE
def fun():
    return 1
</code>
What's the explanation for this behavior?
(This is Python 2.7 on Ubuntu.)


A:

You can't do that because the yield statement (and all the other flow-control constructs) require the function to be interpreted. It does not work on the bytecode level. The CFUNCTYPE creates a C function that is invoked at the bytecode level.

