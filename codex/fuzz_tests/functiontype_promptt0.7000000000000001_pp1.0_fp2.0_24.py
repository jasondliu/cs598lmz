import types
# Test types.FunctionType
def func():
    pass

print(type(func) == types.FunctionType)

# Test types.BuiltinFunctionType
print(type(len) == types.BuiltinFunctionType)

# Test types.LambdaType
print(type(lambda x : x) == types.LambdaType)

# Test types.GeneratorType
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.ModuleType
import sys
print(type(sys) == types.ModuleType)

# Test types.TracebackType
try:
    raise Exception
except:
    ex = sys.exc_info()[2]
    print(type(ex) == types.TracebackType)

# Test types.FrameType
def f():
    import sys
    return sys._getframe()
print(type(f()) == types.FrameType)

# Test types.CodeType
def f(): pass
print(type(f.__code__) == types.CodeType)

# Test types.MappingProxyType
class
