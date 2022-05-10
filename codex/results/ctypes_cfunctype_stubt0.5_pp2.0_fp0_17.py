import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 5

print(fun())
</code>
When I run this code, I get the following error:
<code>Traceback (most recent call last):
  File "C:/Users/Username/Desktop/test.py", line 9, in &lt;module&gt;
    print(fun())
ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: Don't know how to convert parameter 1
</code>
I am using Python 3.6.1 on Windows 10 x64.

