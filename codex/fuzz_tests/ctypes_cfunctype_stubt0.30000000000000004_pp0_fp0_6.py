import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

print fun()
</code>
This works fine, but I want to return a list of strings, and I get a segfault.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ['hello', 'world']

print fun()
</code>
I'm using Python 2.7.3.


A:

I think you need to use <code>ctypes.py_object</code> for each element of the list.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return [ctypes.py_object('hello'), ctypes.py_object('world')]

print fun()
</code>

