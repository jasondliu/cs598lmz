import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class C:
    def method(self, arg):
        return arg

c = C()
inst2 = fun.__get__(c)
print(inst2)
# &lt;ctypes.pythonapi.PyCapsule_Type object at 0x7f3c3ce65410&gt;
</code>
My questions are:

How and why is <code>fun.__get__(c)</code> returning a <code>PyCapsule_Type</code>? Why is it not returning a <code>PyCFunction_Type</code> as in the example above?
How can I get a <code>PyCFunction_Type</code> from <code>fun.__get__(c)</code>?



A:

It looks like it is returning a capsule because it is not a bound method, because you never called <code>types.MethodType</code> on it.
<code>from types import MethodType
from ctypes import py_object, c_void_p, CFUNCTYPE

def fun():
    return None


