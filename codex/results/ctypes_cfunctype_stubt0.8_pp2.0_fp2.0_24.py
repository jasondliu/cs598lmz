import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ob


# this is the expected type:
def fun():
    return ob

print fun
</code>
Unfortunately, I get a TypeError:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: 'CFUNCTYPE' object is not callable
</code>
Any clues on what's going wrong here?


A:

<code>CFUNCTYPE</code> is a class, not an instance, so you can't call it.
When you do <code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)</code>, you're basically saying "create a new anonymous class that inherits from <code>ctypes.CFUNCTYPE</code>" in Python terms. To create an instance of that class, you do <code>FUNTYPE(fun)</code>, where <code>fun</code> is a Python function (in C, it's a pointer to a function).
You can of course give <code>FUNTYPE</code> a
