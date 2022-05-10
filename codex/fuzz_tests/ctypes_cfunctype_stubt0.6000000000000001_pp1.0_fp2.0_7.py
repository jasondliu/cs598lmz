import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"
print fun()
</code>
And I get the following error message:
<code>Traceback (most recent call last):
  File "C:\Users\Fred\Desktop\test.py", line 10, in &lt;module&gt;
    print fun()
TypeError: 'PyCFuncPtrObject' object is not callable
</code>
How can I make this work?


A:

You need to assign the function type to the variable <code>fun</code>.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
fun = FUNTYPE(lambda : "Hello")
print fun()
</code>

