import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    print(fun())
TypeError: 'PyCFuncPtrObject' object is not callable
</code>
I'm not sure why this is happening. I've tried to use <code>ctypes.c_char_p</code> instead of <code>ctypes.py_object</code> but that doesn't work either.


A:

You need to call <code>fun.restype</code> and <code>fun.argtypes</code> to tell ctypes how to call the function. 
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun.restype = ctypes.py_object
fun.argtypes = []

print(fun())
</code>

