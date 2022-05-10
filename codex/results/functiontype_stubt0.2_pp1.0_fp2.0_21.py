from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(type(a.__next__) == types.MethodType)

# 判断一个对象是否是函数
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)

# 使用isinstance()
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 使用dir()
print(dir('ABC'))

# len()
print(len('ABC'))
print(len(b'ABC'))

# 字符串
print('ABC'.encode('ascii'))
print('中文'.encode
