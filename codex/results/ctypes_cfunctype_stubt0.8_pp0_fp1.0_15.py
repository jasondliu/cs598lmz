import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return result.value
f = fun()
del fun
</code>
The <code>del</code> will release the last reference to <code>fun</code>, allowing it to be garbage collected. The <code>fun</code> object will be the only strong reference to <code>result</code> and that difference is enough to make it work.
For the general case, where you are returning a PyObject*, the most correct solution would be to create a new reference and increase its refcount before returning it. In that case, the typical solution would be to use a <code>PyObject*</code> type for the return value of the <code>CFUNCTYPE</code> function.
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return Py_BuildValue("O", result)
</code>
You could also just return the <code>int</code> value and then let the caller create the Python integer object.

