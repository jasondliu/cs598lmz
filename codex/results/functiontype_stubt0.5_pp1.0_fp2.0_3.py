from types import FunctionType
a = (x for x in [1])
print(type(a))
def b():
    yield 1
print(type(b))
print(type(b) == FunctionType)
print(callable(b))
print(callable(a))
print(callable(1))
print(callable("1"))

# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

# print(b.__next__())
# print(b.__next__())
# print(b.__next__())

# print(b.__next__())

# print(b.__next__())

# print(b.__next__())

# print(b.__next__())

# print(b.__next__())

# print(b.__next__())

# print(b.__next__())

# print(b.__next__())

# print(b.__next__())

# print(b.__next__())

# print(b.__next__())

# print(b.
