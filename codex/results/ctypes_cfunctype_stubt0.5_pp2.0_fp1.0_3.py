import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

def run(fun):
    return fun()

print(run(fun))
</code>
Output:
<code>hello world
</code>
The only way I can get this to work is by using <code>CFUNCTYPE</code> instead of <code>WINFUNCTYPE</code>.

