import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hi"

print(fun())
</code>
I get the error
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    print(fun())
TypeError: 'str' does not support the buffer interface
</code>
However, if I change the return value to <code>1</code> instead of <code>"hi"</code>, it works fine.
What is the issue here?


A:

You are returning a <code>bytes</code> object from your function, not a <code>str</code> object.
By default, <code>ctypes</code> interprets the return value as a <code>bytes</code> object. You can change the return type by setting the <code>restype</code> attribute of the <code>CFUNCTYPE</code> object.
<code>FUNTYPE.restype = ctypes.py_object
</code>

