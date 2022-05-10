import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"
print(fun())
</code>
But I get an error:
<code>Traceback (most recent call last):
  File "C:/Users/user/PycharmProjects/untitled/test.py", line 6, in &lt;module&gt;
    print(fun())
TypeError: 'CFUNCTYPE' object is not callable
</code>
I've tried to google this, but I can't find any solution.
How can I fix this?


A:

You have to use the <code>restype</code> argument of <code>CFUNCTYPE</code> to specify the return type of your function.
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
</code>
should be
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, restype=ctypes.py_object)
</code>

