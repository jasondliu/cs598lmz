import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "C:/Users/User/Desktop/test.py", line 8, in &lt;module&gt;
    print(fun())
TypeError: 'PyCFuncPtrObject' object is not callable
</code>
I am using Python 3.7.2.
What am I doing wrong?


A:

You have to call the <code>PyCFuncPtrObject</code> object to get the function object.
<code>print(fun())
</code>
should be
<code>print(fun.__call__())
</code>

