import types
# Test types.FunctionType
def test():
    print('test')

# 返回True
print(type(test) == types.FunctionType)

# 返回True
print(isinstance(test, types.FunctionType))


# Test types.BuiltinFunctionType
# 返回True
print(type(abs) == types.BuiltinFunctionType)

# 返回True
print(isinstance(abs, types.BuiltinFunctionType))

# Test types.LambdaType
# 返回True
print(type(lambda x: x) == types.LambdaType)

# 返回True
print(isinstance(lambda x: x, types.LambdaType))

# Test types.GeneratorType
# 注意到这里要把函数写在前面
print(type(x for x in range(10)) == types.GeneratorType)

# 返回True
print(isinstance((x for x in range(
