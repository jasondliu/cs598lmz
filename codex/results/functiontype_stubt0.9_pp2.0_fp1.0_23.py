from types import FunctionType
a = (x for x in [1])
b = 1,
c = [554, 338, 332, 419, 270]
d = dic = dict(a = 1, b = 2, c = 3)
e = False
f = frozenset(a)
g = str = 'hello'
h = m = object
j = complex = complex(1)
k = set(b)
l = func = function = FunctionType(lambda x: x, {})

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(j))
print(type(k))
print(type(l))

class Test:
    pass
test = Test()
print(type(test))
print()

# 结果
# <class 'generator'>
# <class 'tuple'>
# <class 'list'>
# <class 'dict'>
# <class 'bool'>
# <class 'frozenset
