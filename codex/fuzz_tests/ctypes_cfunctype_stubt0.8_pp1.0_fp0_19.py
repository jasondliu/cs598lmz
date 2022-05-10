import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return None
fun()
</code>
It raises a <code>TypeError</code> :
<code>TypeError: an integer is required
</code>
Is it a bug of <code>ctypes</code> ? If not, how can we return <code>None</code> ?

