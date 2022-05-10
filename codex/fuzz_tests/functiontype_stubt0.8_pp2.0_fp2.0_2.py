from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == types.MethodType)
print(isinstance(a.__next__, FunctionType))

print("\n------comprehension------")
s = {x for x in list(range(10))}
print(s)

print("\n------tuple------")
s = (x for x in list(range(10)))
t = 3, 4, 5
f = (3, 4, 5)
print(t)
print(type(t))
print(f)
print(type(f))
print(s)
print(type(s))
print(list(s))
print(type(list(s)))
print(tuple(s))
print(type(tuple(s)))

print("\n------list------")
s = [x for x in list(range(10))]
t = [3, 4, 5]
print(t)
print(type(t))
print(s)
print
