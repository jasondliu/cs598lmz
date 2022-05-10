import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

fun()()

# This doesn't work
class Base:
    def __call__(self):
        return None

class Derived(Base):
    def __call__(self):
        return 42

fun = FUNTYPE(Derived)()
fun()
</code>
The second example thrashes the stack and crashes python. Is there some way to fix this without writing a C wrapper?


A:

The method object produced by PyObject_GetAttrString() is a bound method, so it already has an implicit <code>self</code>. You can't just directly use it as a C callback function because it expects two PyObjects to be passed to the callable, not one.
You can fix this by calling the unbound method PyObject_GetAttrString(type_spec, name) instead, this returns a simpler function object that works well with CFUNCTYPE.
Here is a working version of your second example:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

class Base:
    def __call__
