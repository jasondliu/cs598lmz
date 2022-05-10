import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'foo'

try:
    fun(None, None)
except Exception as ex:
    print(ex)

try:
    fun(None, None, None)
except Exception as ex:
    print(ex)
</code>
Output:
<code>fun() takes exactly 0 arguments (2 given)
fun() takes exactly 0 arguments (3 given)
</code>

