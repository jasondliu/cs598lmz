import types
# Test types.FunctionType
def foo():
    pass

print(type(foo))
print(type(foo) == types.FunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(abs) == types.BuiltinFunctionType)
print(type(int) == types.BuiltinFunctionType)

# Test types.MethodType
import math
print(type(math.pow) == types.BuiltinMethodType)

# Test types.UnboundMethodType
print(type(math.pow) == types.UnboundMethodType)

# Test types.ModuleType
print(type(math) == types.ModuleType)

# Test types.TracebackType
try:
    raise Exception('error')
except Exception as e:
    print(type(e.__traceback__) == types.TracebackType)

# Test types.FrameType
def bar():
    b = 1

print(type(bar
