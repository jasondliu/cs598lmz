import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 3

fun()
</code>
I get the following error:
<code>$ python test.py
Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    fun()
TypeError: argument 1 must be string or read-only character buffer, not int
</code>
I have no idea about what is going wrong here. 
I am running Python 2.7.5 on Ubuntu 13.10.


A:

You are not telling ctypes that your function returns an <code>int</code>:
<code>&gt;&gt;&gt; FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
&gt;&gt;&gt; FUNTYPE(fun)()
3
</code>

