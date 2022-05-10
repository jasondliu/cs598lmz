import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Hello World")
    return 3

fun()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "random_test.py", line 9, in &lt;module&gt;
    fun()
TypeError: &lt;built-in function fun&gt; returned a result with an error set
</code>
I am using Python 3.8.2. Any help would be appreciated.


A:

A <code>CFUNCTYPE</code> function returning a <code>py_object</code> must return <code>NULL</code> on error instead of an integer. The <code>NULL</code> object is <code>Py_None</code>, which is pre-defined for you.
<code>from ctypes import *

def fun():
    print("Hello World")
    return Py_None

FUNTYPE = CFUNCTYPE(py_object)
cfun = FUNTYPE(fun)
cfun()
</code>

