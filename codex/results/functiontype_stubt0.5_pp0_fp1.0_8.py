from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
c = a
print(a is b)
print(a is c)
print(a == b)
print(a == c)

print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(a.__next__())

# 列表生成器
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])
print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# 生成器
g = (x * x for x
