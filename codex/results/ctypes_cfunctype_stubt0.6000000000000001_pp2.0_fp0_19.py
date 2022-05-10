import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello world'

def g():
    return 'hello world'

print fun.__name__
print g.__name__
</code>
The output is:
<code>fun
g
</code>
I expected the output to be:
<code>fun
fun
</code>

