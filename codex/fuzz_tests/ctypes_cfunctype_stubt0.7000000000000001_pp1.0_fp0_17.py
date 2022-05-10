import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"
assert fun() == "fun"
</code>
Output:
<code>Traceback (most recent call last):
  File "fun.py", line 6, in &lt;module&gt;
    assert fun() == "fun"
TypeError: argument 1 must be string without null bytes, not str
</code>
The above error is raised by CPython's <code>PyString_FromString</code> function. So I tried this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun".encode()
assert fun() == "fun"
</code>
and got the following error:
<code>Traceback (most recent call last):
  File "fun.py", line 6, in &lt;module&gt;
    assert fun() == "fun"
AssertionError
</code>
So it looks like <code>PyString_FromString</code> is being called under the hood, and it's failing. It's not clear to me
