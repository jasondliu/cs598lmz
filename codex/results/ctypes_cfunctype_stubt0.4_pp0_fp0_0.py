import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

print fun()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "C:/Users/jared/Desktop/test.py", line 8, in &lt;module&gt;
    print fun()
TypeError: object of type 'PyCFuncPtrType' has no len()
</code>
I'm not sure what I'm doing wrong.  I've tried changing the return type to <code>ctypes.c_char_p</code> and <code>ctypes.c_void_p</code> with no luck.  I'm not sure what I'm doing wrong.  I'm using Python 2.7.2.


A:

The problem is that you are returning a string from a function that is declared to return a Python object.  The return type of the function is a Python object, so you need to return a Python object.  You can do that by wrapping the string in a Python object:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@
