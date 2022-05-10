import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
The error message is:
<code>Traceback (most recent call last):
  File "C:\Users\user\Desktop\test.py", line 10, in &lt;module&gt;
    print(fun())
ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: wrong type
</code>
I have tried to use <code>ctypes.c_char_p</code> instead of <code>ctypes.py_object</code> but it didn't work.
I have also tried to use <code>ctypes.c_char_p</code> and <code>ctypes.c_char_p(fun())</code> but it didn't work.
I have also tried to use <code>ctypes.c_char_p</code> and <code>ctypes.c_char_p(str(fun()))</code> but it didn't work.
I have also tried to use <code>ctypes.c_char_p</code> and <code>ct
