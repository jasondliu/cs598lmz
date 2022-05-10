import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()

print type(fun)
</code>
Output
<code>hello
&lt;type '_ctypes.CFuncPtr'&gt;
</code>
Here is another example without <code>ctypes.py_object</code>
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
@FUNTYPE
def fun():
    return "hello"

print fun()

print type(fun)
</code>
Output
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    def fun():
TypeError: don't know how to convert return value
</code>

