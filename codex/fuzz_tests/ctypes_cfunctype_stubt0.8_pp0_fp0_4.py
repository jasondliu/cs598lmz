import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

fun()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
OSError: exception: access violation reading 0x00000004
</code>


A:

I was able to solve this by declaring the return type as <code>ctypes.c_long</code>, then converting the returned value to Long:
<code>import ctypes

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_long)

@FUNTYPE
def fun():
    return 0

fun()
# 0L
</code>

