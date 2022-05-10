import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
xxx = fun()
print xxx
</code>
It seems to do nothing; I'm on Windows with Python 2.7. What's the problem? I had no problems with plain py_object like above.

