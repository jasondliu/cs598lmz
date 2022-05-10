from types import FunctionType
a = (x for x in [1])
print(type(a) == GeneratorType)
print()

b = (x for x in [1])
print(isinstance(b, GeneratorType))
print()

c = (x for x in [1])
print(isinstance(c, Iterable))
print(isinstance(list(c), Iterable))
print()

d = (x for x in [1])
print(isinstance(d, Iterator))
print(isinstance(list(d), Iterable))
print(isinstance(list(d), Iterator))
print()

# list() 可以把任意 Iterable 轉為 list
# 但是不可以把 Iterator 轉為 List

for i in (x for x in [1]):
    print(i)
print()

e = (x for x in [1])
f = list(e)
print(f)
print()

g = (x for x in [1])
print(list(g))
print(list(g
