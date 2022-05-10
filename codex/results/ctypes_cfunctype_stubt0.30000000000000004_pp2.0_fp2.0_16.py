import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

fun()
</code>
This works, but I don't know how to make it work with a function that takes arguments. I tried the following:
<code>@FUNTYPE
def fun(a):
    return a

fun(42)
</code>
But this gives the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: fun() takes exactly 1 argument (2 given)
</code>
I also tried the following:
<code>@FUNTYPE(ctypes.py_object, ctypes.py_object)
def fun(a):
    return a

fun(42)
</code>
But this gives the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: fun() takes exactly 1 argument (2 given)
</code>
How can I get this to work?


A:

I
