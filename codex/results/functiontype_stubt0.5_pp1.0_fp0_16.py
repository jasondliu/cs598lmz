from types import FunctionType
a = (x for x in [1])
print(a)

# 测试函数是否是可调用对象
print(callable(a))
print(callable(max))
print(callable([1,2,3]))
print(callable(None))
print(callable('str'))

# 测试是否是一个函数
print(isinstance(abs,FunctionType))
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

# 测试是否是某几种类型
print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))

# 使用dir()函数
print(dir('ABC'))

# 使用getattr()
