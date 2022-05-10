import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 5

print fun()
</code>
This yields the error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    print fun()
ctypes.ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: wrong type
</code>
What am I doing wrong?


A:

The only way I found to get this to work is to use the <code>_as_parameter_</code> attribute of the <code>ctypes.py_object</code> instance:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 5

print fun._as_parameter_()
</code>
This works, but it's kind of a hack, so I'm hoping someone has a better solution.

