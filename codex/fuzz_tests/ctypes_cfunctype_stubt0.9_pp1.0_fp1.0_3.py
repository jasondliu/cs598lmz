import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
</code>
Unfortunately, this example doesn't work as it is.  Why is that?  And how could it be repaired?


A:

<code>pyfunc = ctypes.pythonapi.PyCFunction_NewEx(cfun, ob, NULL)
</code>
is equivalent to:
<code>pyfunc = cfun(NULL)
</code>
i.e. more or less
<code>def pyfunc():
    return NULL
</code>
which is why you get <code>None</code> as the result.

Nothing in the documentation tells you that <code>PyCFunction_NewEx</code> returns a PyCFunction object. (as opposed to PyCFunctionObject)
Neither does the documentation tell you that you have to pass a PyCFunctionObject to PyFunction_New,
nor that a PyCFunction is not a regular Python function (i.e., a PyFunctionObject)
nor that you need the <code>CFUNCTYPE</code> wrapper in the first place.

The documentation leaves a few things to guess and to experiment:

a PyC
