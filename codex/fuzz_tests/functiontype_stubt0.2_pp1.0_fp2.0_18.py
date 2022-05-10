from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(abs))
print(type(a) == types.GeneratorType)
print(type(lambda x: x) == types.LambdaType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.FunctionType)
print(type(abs) == FunctionType)

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
# >>> import types
# >>> def fn():
# ...     pass
# ...
# >>> type(fn)==types.FunctionType
# True
# >>> type(abs)==types.Builtin
