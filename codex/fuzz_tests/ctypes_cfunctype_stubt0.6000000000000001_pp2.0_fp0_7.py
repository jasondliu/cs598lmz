import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

print(fun())
</code>
I get the following error message:
<code>Traceback (most recent call last):
  File "/home/me/test.py", line 12, in &lt;module&gt;
    print(fun())
SystemError: &lt;built-in function fun&gt; returned a result with an error set
</code>
What's going on here? What am I doing wrong?


A:

The error is due to this bug in <code>ctypes</code>: https://bugs.python.org/issue22995
The workaround is to not use <code>ctypes.py_object</code> as the return type. 
For example:
<code>#!/usr/bin/python3

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
@FUNTYPE
def fun():
    return 1

print(fun())
</code>

