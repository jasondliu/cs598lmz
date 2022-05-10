import types
# Test types.FunctionType
def func():
    pass

print(type(func) is types.FunctionType)
print(type(lambda x: x) is types.LambdaType)
print(type((x for x in range(10))) is types.GeneratorType)

# Test types.BuiltinFunctionType
import sys
print(type(len) is types.BuiltinFunctionType)
print(type(sys.exit) is types.BuiltinFunctionType)

# Test types.MethodType
class A:
    def func(self):
        pass

a = A()
print(type(a.func) is types.MethodType)

# Test types.ModuleType
import types
print(type(types) is types.ModuleType)

# Test types.TracebackType
import sys
try:
    1/0
except:
    tb = sys.exc_info()[2]
    print(type(tb) is types.TracebackType)

# Test types.FrameType
def func():
    return sys._getframe()

frame = func()
print(
