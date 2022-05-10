from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type((x for x in [1])))
print(type(FunctionType))
print(type(lambda x: x))
print(type(abs))
print(type(a) == types.GeneratorType)
print(type(a) == type((x for x in [1])))
print(type(a) == type([]))
print(type(a) == type(()))
print(type(a) == type({}))
print(type(a) == type(123))
print(type(a) == type('str'))
print(type(a) == type(b'abc'))
print(type(a) == type(None))

# 类型判断
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# dir()
print(dir('ABC'))
print('ABC'.__len__())
print(len('ABC'))
print(len(123))
print(len((1
