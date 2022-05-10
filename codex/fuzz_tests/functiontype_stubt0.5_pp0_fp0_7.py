from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(a.__next__())
print(a.__next__())

def b():
    yield 1
    yield 2

print(b.__next__)
print(type(b.__next__) == FunctionType)
print(b().__next__())
print(b().__next__())

print(type(b()))
print(type(b()) == FunctionType)

c = b()
print(c.__next__())
print(c.__next__())
print(c.__next__())
