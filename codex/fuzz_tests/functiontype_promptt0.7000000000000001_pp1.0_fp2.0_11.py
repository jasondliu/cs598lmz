import types
# Test types.FunctionType
def some_func():
    pass
print(type(some_func) == types.FunctionType) # True
# Test types.ModuleType
import math
print(type(math) == types.ModuleType) # True
print(type(math.sin) == types.BuiltinFunctionType) # True
print(type(math.cos) == types.BuiltinFunctionType) # True
print(type(math.tan) == types.BuiltinFunctionType) # True
