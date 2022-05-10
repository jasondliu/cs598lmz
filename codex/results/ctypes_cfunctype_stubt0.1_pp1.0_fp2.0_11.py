import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
This works fine, but I would like to be able to return a string that is not a constant.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello" + "world"

print(fun())
</code>
This fails with the error:
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    print(fun())
  File "test.py", line 4, in fun
    return "hello" + "world"
TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
</code>
I have also tried using <code>ctypes.c_char_p</code> as the return type, but this fails with the same error.
How can I return a string that is not a constant?


A:

You can't.  The <code>CFUNCTYPE</code
