import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello world'

print fun()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: 'PyCFunction' object is not callable
</code>
How can I make this work?


A:

You need to call the <code>PyCFunction_NewEx</code> function to create a callable <code>PyCFunctionObject</code> object.
<code>import ctypes

FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

@FUNTYPE
def fun():
    return 'hello world'

fun = ctypes.pythonapi.PyCFunction_NewEx(fun, None, None)

print(fun())
</code>

