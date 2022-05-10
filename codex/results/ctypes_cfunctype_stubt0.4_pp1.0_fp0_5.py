import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World!"

fun()
</code>
The error message is:
<code>Traceback (most recent call last):
  File "C:/Users/User/PycharmProjects/untitled/test.py", line 8, in &lt;module&gt;
    fun()
TypeError: 'PyCFuncPtrObject' object is not callable
</code>
What is the problem?


A:

You need to assign the function to a variable, then call the variable.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

@FUNTYPE
def fun():
    return "Hello World!"

f = fun
f()
</code>

