import types
# Test types.FunctionType
def f():
    pass

print(type(f) == types.FunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(len) == types.BuiltinFunctionType)
print(type(iter) == types.BuiltinFunctionType)

# Test types.MethodType
print(type(''.join) == types.BuiltinMethodType)

# Test types.UnboundMethodType
import random
print(type(random.shuffle) == types.UnboundMethodType)

# Test types.ModuleType
import sys
print(type(sys) == types.ModuleType)

# Test types.TracebackType
try:
    raise Exception()
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(type(exc_traceback) == types.TracebackType)

# Test types.FrameType
def g():
    import sys
