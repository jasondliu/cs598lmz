import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

print(fun())
</code>
This is the error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    print(fun())
TypeError: 'int' object is not callable
</code>
It seems that <code>fun</code> is an <code>int</code> type.
What's wrong?


A:

You're not calling your function. You're returning an int from it. Try this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return fun

print(fun()())
</code>

