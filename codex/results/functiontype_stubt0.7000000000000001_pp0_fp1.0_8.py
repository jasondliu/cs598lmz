from types import FunctionType
a = (x for x in [1])
print(a)
print(a.__next__())
print(a.__next__())

def test():
    yield 1
    yield 2
    yield 3

t = test()
print(t)
print(t.__next__())
print(t.__next__())
print(t.__next__())

print(type(a))
print(type(t))
print(type(print))
print(type(type))
print(type(FunctionType))

print(type(a) == GeneratorType)
print(type(t) == GeneratorType)
print(type(print) == FunctionType)
print(type(type) == FunctionType)
print(type(FunctionType) == FunctionType)
