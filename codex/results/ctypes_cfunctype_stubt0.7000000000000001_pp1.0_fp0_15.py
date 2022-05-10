import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
print(fun())
</code>
Output:
<code>hello
</code>

We can find out more about our function using <code>dir</code> function:
<code>dir(fun)
</code>
Output:
<code>['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_flags_', '_restype_', '_needs_freeing_', '_objects_', '_paramflags_', '_paramtypes_', '_paramnames_', '_paramvalues_', '_result
