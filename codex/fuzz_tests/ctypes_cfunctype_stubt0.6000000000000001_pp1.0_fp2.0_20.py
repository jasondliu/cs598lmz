import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
fun()
</code>
The problem is that the function <code>fun</code> is not called as if it was a Python function. Indeed, if I call <code>fun()</code> I get <code>hello</code>, while if I call <code>fun.__call__()</code> I get <code>&lt;__main__.fun object at 0x7f5e5b5d5f98&gt;</code>.
I would like to be able to call <code>fun</code> as if it was a Python function. I tried to call <code>fun.__call__()</code> but it does not work. 
My goal is to use <code>fun</code> in a <code>Cython</code> module.
I am using Python 3.6.


A:

This works for me:
<code>from ctypes import *

FUNTYPE = CFUNCTYPE(py_object)

@FUNTYPE
def fun():
    return "hello"

print(fun.__call__())
</code>

