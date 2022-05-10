import types
# Test types.FunctionType
def func():
    pass

print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.LambdaType
# 可以判断函数是否为lambda函数，但不能判断函数是否为普通函数
# 因为普通函数也是可以判断的

# Test types.GeneratorType
# 可以判断函数是否为生成器，但不能判断函数是否为普通函数
# 因为普通函数也是可以
