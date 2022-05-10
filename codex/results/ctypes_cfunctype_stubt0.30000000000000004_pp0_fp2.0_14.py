import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

print fun()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "C:\Users\user\Desktop\test.py", line 9, in &lt;module&gt;
    print fun()
ctypes.ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: expected LP_CFUNCTYPE instance instead of CFUNCTYPE
</code>
I am using Python 2.7.3.


A:

You need to pass the function object as the first argument to <code>CFUNCTYPE</code>, not the return value of the function:
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(x):
    return "Hello"
</code>

