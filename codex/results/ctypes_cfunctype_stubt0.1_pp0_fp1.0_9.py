import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
This works fine, but I want to be able to return a string that is not a literal.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello" + "world"

print(fun())
</code>
This gives me the following error:
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    print(fun())
  File "test.py", line 4, in fun
    return "hello" + "world"
TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
</code>
I have tried using <code>ctypes.c_char_p</code> instead of <code>ctypes.py_object</code>, but that gives me a different error:
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt
