import types
# Test types.FunctionType, types.BuiltinFunctionType, types.BuiltinMethodType, types.MethodType, types.ClassType, types.UnboundMethodType, types.InstanceType
def f(): pass

print type(f) is types.FunctionType
print type(oct) is types.BuiltinFunctionType
print type(str.replace) is types.MethodType
print type(str) is types.ClassType
print type(str.replace) is types.UnboundMethodType
print type("abc") is types.InstanceType

print type(oct)


def f():
    def g():
        return "inner"
    return g

g1 = f()
print g1
print g1()
print f.func_closure
print g1.func_code
print g1.func_code.co_name
print g1.func_code.co_varnames
print g1.func_code.co_argcount


# Test inspect.isclass and inspect.isroutine
print "\nCallable objects"
import inspect
def f(x): return x
class C(object):
    def
