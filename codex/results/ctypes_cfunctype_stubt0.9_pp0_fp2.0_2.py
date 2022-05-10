import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return 0
import numpy
a = numpy.zeros(2)
fun()
</code>
The following error happens :
<code>myfun()
ctypes.ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: Don't know how to convert parameter 1
</code>
A similar error does not happen if I use simply a python function
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
def fun2():
  return 0
fun3 = FUNTYPE(fun2)
import numpy
a = numpy.zeros(2)
fun3()
</code>
Do you know why a python function can be called using its decorator but not a cython function?
Thank you.


A:

There are a couple of issues:

Your Cython function returns <code>int</code>, but the corresponding Python function is supposed to return <code>object</code>, hence your later error about not knowing how to convert a function parameter.
You should define your function as a "pure" C
