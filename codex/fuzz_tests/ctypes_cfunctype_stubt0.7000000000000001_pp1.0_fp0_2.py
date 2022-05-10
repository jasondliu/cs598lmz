import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"
# This doesn't work.
class C(object):
    def __init__(self):
        self._fun = fun

c = C()
print(c._fun)
</code>
It gives me this error:
<code>Traceback (most recent call last):
  File "test.py", line 15, in &lt;module&gt;
    c = C()
  File "test.py", line 10, in __init__
    self._fun = fun
ctypes.ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: expected CFUNCTYPE instance instead of builtin_function_or_method
</code>
I can't use <code>CFUNCTYPE(ctypes.py_object, ctypes.py_object)</code> because I don't know how many arguments it will have.
How can I make this work?


A:

The problem is that <code>fun</code> is not a <code>CFUNCTYPE</code> instance.  It's a Python function that
