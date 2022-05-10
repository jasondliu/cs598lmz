import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
print fun()
</code>
This gives me the error:
<code>TypeError: 'CFUNCTYPE' object is not callable
</code>
I'm not sure what I'm doing wrong.


A:

<code>CFUNCTYPE</code> is a class. You have to create an instance of it.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE()
def fun():
    return "hello"
print fun()
</code>

