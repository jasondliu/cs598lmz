import types
# Test types.FunctionType
def func():
    pass
print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
# >>> import types
# >>> def fn():
# ...     pass
# ...
# >>> type(fn)==types.FunctionType
# True
# >>> type(abs)==types.BuiltinFunctionType
# True
# >>> type(lambda x: x)==types.LambdaType
# True
