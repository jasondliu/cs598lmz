import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun in dll"
dll.func = fun
dll.func()
</code>
the output is :
<code>&gt;&gt;&gt; dll.func()
fun in dll
</code>
But I have got an error when I have tried to access the return value.
<code>&gt;&gt;&gt; a = dll.func()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ValueError: Procedure probably called with not enough arguments (4 bytes missing) or wrong calling convention
</code>
I have tried to add a parameter in the function and it works.
<code>&gt;&gt;&gt; @FUNTYPE
... def fun(a):
...     return "fun in dll"
... 
&gt;&gt;&gt; dll.func = fun
&gt;&gt;&gt; dll.func()
fun in dll
&gt;&gt;&gt; a = dll.func()

