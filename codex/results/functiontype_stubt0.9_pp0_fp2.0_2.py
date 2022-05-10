from types import FunctionType
a = (x for x in [1])


def f():
    return
print(a)
print(type(a))
print(type(f))
print(type(type(a)))
print(type(f()) == int)
print(isinstance(f, FunctionType))

f.a = 'abc'
print(f.a)

print(isinstance(a, GeneratorType))


class Cls:
    pass


print(isinstance(Cls, type))
