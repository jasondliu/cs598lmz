from types import FunctionType
a = (x for x in [1])
a.__next__()

# 获取对象信息
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
print(type(a))

print(type(123) == int)
print(type('str') == str)
print(type(None) == type(123))
print(type(abs) == types.BuiltinFunctionType)
print(type(a) == types.GeneratorType)

# 使用isinstance()
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 使用dir()
print(dir('ABC'))
print('ABC'.lower())
print('ABC'.__len__())
print(len('ABC'))
print('ABC'.capitalize())

# 类
