import types
# Test types.FunctionType
def check(x):
    if type(x) == types.FunctionType:
        return "func"
    elif type(x) == types.BuiltinFunctionType or type(x) == types.BuiltinMethodType:
        return "builtin"
    else:
        return "type error"

check(myclass.mymethod)
# Test types.MethodType
m = myclass.mymethod
check(m)
# Test types.TypeType
check(type(myclass))

# Test isinstance
class X:
    pass
x = X()
isinstance(x, X)
isinstance(x, types.InstanceType)
isinstance(myclass, myclass)
isinstance(myclass, type)
isinstance(myclass(), myclass)

# Test types.NoneType
import weakref
def test():
    yield None
# since generators are not collectiable, we have to make a
# weak reference to it, else we can't test the gc behaviour
w = weakref.ref(test())
# This will invoke the garbage collector, which in turn must
