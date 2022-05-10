from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(a.__next__)
print(a.__next__())

# generator
def gen():
    yield 1
    yield 2
    yield 3

print(gen)
print(gen())
b = gen()
print(b)
print(type(b))
print(type(b.__next__))
print(type(b.__next__) == FunctionType)
print(b.__next__)
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())

# generator2
def gen2():
    for i in range(5):
        yield i

print(gen2)
print(gen2())
b2 = gen2()
print(b2)
print(type(b2))
print(type(b2.__next__))
print(type(b2.__next__) == FunctionType)
