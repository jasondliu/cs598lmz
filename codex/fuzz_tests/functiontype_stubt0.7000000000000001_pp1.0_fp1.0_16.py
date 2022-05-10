from types import FunctionType
a = (x for x in [1])
b = int
c = lambda x: x
d = FunctionType
e = int.__new__
f = FunctionType.__new__
g = lambda x: x.__new__
h = property
i = property.__new__
j = property.__call__
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))

# <class 'generator'>
# <class 'type'>
# <class 'function'>
# <class 'type'>
# <class 'method'>
# <class 'method'>
# <class 'function'>
# <class 'type'>
# <class 'method'>
# <class 'method'>

# 显示出generator和property并不属于普通类型，而是并不属
