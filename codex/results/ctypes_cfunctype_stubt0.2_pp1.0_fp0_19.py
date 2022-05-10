import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
This works fine.
But if I try to return a list, I get an error:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return [1,2,3]

print fun()
</code>
This gives the error:
<code>TypeError: 'list' does not have the buffer interface
</code>
How can I return a list?


A:

You need to use <code>ctypes.py_object</code> as the return type:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return [1,2,3]

print fun()
</code>

