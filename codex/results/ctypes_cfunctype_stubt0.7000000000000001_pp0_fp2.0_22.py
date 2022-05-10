import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
print fun()
</code>
This returns <code>42</code> as expected.
But if I try to return a list:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return [42]
print fun()
</code>
I get an exception:
<code>Traceback (most recent call last):
  File "c.py", line 7, in &lt;module&gt;
    print fun()
  File "c.py", line 6, in fun
    return [42]
SystemError: &lt;built-in function fun&gt; returned a result with an error set
</code>


A:

<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
&gt;&gt;&gt; @FUNTYPE
... def fun():
...     return [42]
... 
&gt;&gt
