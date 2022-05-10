import types
# Test types.FunctionType
def foo():
    pass
foo

types.FunctionType(foo.__code__, foo.__globals__)

# Test types.MethodType
class A:
    def foo(self):
        pass
a = A()
a.foo
types.MethodType(a.foo.__func__, a)

# Test types.ClassType
class B:
    pass
b = B()
types.ClassType(B.__name__, B.__bases__, B.__dict__)

# Test types.InstanceType
types.InstanceType(B)

# Test types.UnboundMethodType
a.foo.__self__ = None
types.UnboundMethodType(a.foo.__func__, b)

# Test types.BuiltinFunctionType
def bar():
    pass
types.BuiltinFunctionType(bar.__code__)

# Test types.BuiltinMethodType
int.__call__
types.BuiltinMethodType(int.__call__.__func__, int)

# Test types.ModuleType
import types

