import types
# Test types.FunctionType
def func(): pass
print isinstance(func, types.FunctionType) # True

# Test types.LambdaType
print isinstance((lambda x: x), types.LambdaType) # True

# Test types.GeneratorType
print isinstance((x for x in range(10)), types.GeneratorType) # True

# Test types.CodeType
print isinstance(func.func_code, types.CodeType) # True

# Test types.FrameType
def func():
    print isinstance(sys._getframe(), types.FrameType) # True
func()

# Test types.TracebackType
try:
    1/0
except:
    print isinstance(sys.exc_info()[2], types.TracebackType) # True

# Test types.BuiltinFunctionType
print isinstance(len, types.BuiltinFunctionType) # True

# Test types.BuiltinMethodType
print isinstance([].append, types.BuiltinMethodType) # True

# Test types.ModuleType
import types
print isinstance(types, types.
