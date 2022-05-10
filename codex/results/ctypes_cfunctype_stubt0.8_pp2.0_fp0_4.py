import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

print(fun())
# 'hello world'
print(type(fun))
# <class 'ctypes.CFUNCTYPE'>
print(type(fun(None)))
# &lt;class 'bytes'&gt;
</code>
The built-in function <code>repr</code> uses the <code>PyObject</code>'s <code>__repr__</code> method to obtain a representation of the object in the form of a string, which allows the strigified result to go through the normal string conversion to unicode.
<code>print(repr(fun()))
# 'hello world'
print(type(repr(fun())))
# &lt;class 'str'&gt;
</code>

