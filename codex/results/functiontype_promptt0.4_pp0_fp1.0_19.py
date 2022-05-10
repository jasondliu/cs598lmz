import types
# Test types.FunctionType
def func():
    pass

print(type(func) == types.FunctionType)
# Test types.LambdaType
lamb = lambda x: x**2
print(type(lamb) == types.LambdaType)
# Test types.GeneratorType
def gen():
    yield 1

print(type(gen()) == types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(print) == types.BuiltinFunctionType)
# Test types.BuiltinMethodType
print(type(str.upper) == types.BuiltinMethodType)
# Test types.MethodType
class A:
    def method(self):
        pass

print(type(A.method) == types.MethodType)
# Test types.ModuleType
import sys
print(type(sys) == types.ModuleType)
# Test types.TracebackType
try:
    raise Exception
except:
    print(type(sys.exc_info()[2]) == types.TracebackType)
# Test types.FrameType
def f():
    print(
