import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

fun is fun.__call__ # for this test
</code>
The rest
<code>import sys
print(fun())
print(sys.getrefcount(fun)
</code>
will output
<code>42
11 # it is 10 and more
</code>


A:

<code>sys.getrefcount()</code> counts the parameter you passed in, too.  And it calls <code>Py_INCREF</code> internally which increments the reference count by one.  So the result depends on whether the reference count was already 1, in which case it would show 2.  Otherwise, adding 1 to "10 and more" is going to be 11.

Here's a test:
<code>import ctypes
from sys import getrefcount as grc

ctypes.py_object(None)   # =&gt;  1
grc(None)                # =&gt;  2
</code>

