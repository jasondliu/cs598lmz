from types import FunctionType
a = (x for x in [1])
b = [1, 2, 3]
c = {1, 2, 3}
d = {'a': 1, 'b': 2}
e = FunctionType(lambda x=1: x, {})
f = int
g = type(None)
h = type
print(a, b, c, d, e, f, g, h)

print('*' * 10, '以下为类型的方法属性', '*' * 10)
print('type', type(type))
print('type.__name__', type.__name__)
print('type.__mro__', type.__mro__)
print('type.__orig_bases__', type.__orig_bases__)
print('type.__bases__', type.__bases__)
print('type.__base__', type.__base__)
print('type.__subclasses__', type.__subclasses__())
print('type.__call__', type.__call__)
print('type.__dict__
