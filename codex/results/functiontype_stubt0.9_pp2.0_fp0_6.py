from types import FunctionType
a = (x for x in [1])
b = (x for y in [1])

# def f():
#     return 1
#
# f.__name__ = 'changed'

print(type(a) == type(b))
print(a.gi_code == b.gi_code)

print(type(a))
print(type(b))
# print(type(f))


g = type(a)

c = g(y for y in [2])
print(c.gi_code)
print(c.gi_code == a.gi_code)
