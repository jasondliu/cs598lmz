from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)

for value in a:
    print(value)
for value in a:
    print(value)

print((lambda x:x) is FunctionType)


print()


def add(a, b=1):
    return a + b


print(add(2))
print(add(2, 2))

s = lambda a, b=3: a + b

print(s(1, 2))
print(s(1))
print(s.__annotations__)

print(add)

print(id(add))
print(id(s))
print(id(lambda a, b=3: a + b))

print(add.__name__)
print(s.__name__)
print((lambda a, b=3: a + b).__name__)

print(id(add.__code__))
print(id(s.__code__))
print(id((lambda a, b=3: a + b).__code__))

print
