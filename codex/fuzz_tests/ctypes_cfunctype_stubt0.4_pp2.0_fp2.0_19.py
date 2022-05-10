import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "/home/user/Documents/test.py", line 7, in &lt;module&gt;
    print(fun())
TypeError: 'CFUNCTYPE' object is not callable
</code>
However, if I change the return type to <code>ctypes.c_char_p</code> it works:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
I have tried all the other return types from the <code>ctypes</code> module, but none of them work.
What am I doing wrong?


A:

The problem is that <code>ctypes.c_char_p</code> is a pointer type, and <code>ctypes</code> handles the conversion of the return value for you.  <code>ctypes.
