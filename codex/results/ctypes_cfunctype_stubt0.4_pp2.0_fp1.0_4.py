import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

print(fun())
</code>
I get this error:
<code>Traceback (most recent call last):
  File "C:\Users\paul\Desktop\test.py", line 6, in &lt;module&gt;
    print(fun())
TypeError: 'PyCFuncPtrObject' object is not callable
</code>
What am I doing wrong?


A:

You need to pass the address of the function to <code>CFUNCTYPE</code>:
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(arg):
    return 'hello'

print(fun(None))
</code>

