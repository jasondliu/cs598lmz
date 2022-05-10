import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
This is the error I get:
<code>Traceback (most recent call last):
  File "C:\Users\User\Desktop\test.py", line 8, in &lt;module&gt;
    print(fun())
  File "C:\Python27\lib\ctypes\__init__.py", line 366, in __call__
    return self.call(args)
ctypes.ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: wrong type
</code>
What am I doing wrong?


A:

I think you need to use <code>ctypes.c_char_p</code> instead of <code>ctypes.py_object</code> for the return type.

