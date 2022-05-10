import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
print(fun())
</code>
This works on CPython, but not on PyPy, where I get the error
<code>TypeError: 'CFUNCTYPE' object is not callable
</code>
Does anyone know how to call C functions from PyPy?


A:

PyPy does not support ctypes.
See http://doc.pypy.org/en/latest/faq.html#what-is-the-status-of-ctypes

