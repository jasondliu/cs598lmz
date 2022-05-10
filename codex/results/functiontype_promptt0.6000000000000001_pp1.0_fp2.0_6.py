import types
# Test types.FunctionType
def func_test():
    pass
print(type(func_test) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 测试实例
print("------------------------------")
import sys
def fn():
    pass
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)
print(type(x for x in range(10)) == types.GeneratorType)
print(type(sys) == types.ModuleType)

# isinstance
print("------------------------------")
import types
def fn():
    pass
print(isinstance(fn, types.FunctionType))
print(isinstance(abs, types.BuiltinFunctionType))

