from types import FunctionType
a = (x for x in [1])
print(type(a))

b = FunctionType(a, globals())
print(type(b))

c = b()
print(type(c))

print(c.__next__())

print(c.__next__())

# print(c.__next__())

# print(c.__next__())

# print(c.__next__())

# print(c.__next__())

# print(c.__next__())

# print(c.__next__())

# print(c.__next__())

# print(c.__next__())

# print(c.__next__())

# print(c.__next__())

# print(c.__next__())

# print(c.__next__())

# print(c.__next__())

# print(c.__next__())

# print(c.__next__())

# print(c.__next__())

# print(c.__next__())

# print(c.__next
