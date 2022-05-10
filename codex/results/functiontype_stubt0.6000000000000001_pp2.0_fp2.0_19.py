from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

b = FunctionType(x for x in [1])
print(b)
print(type(b))

# c = (x for x in [1])()
# print(c)
# print(type(c))

# d = (x for x in [1])()()
# print(d)
# print(type(d))

# e = (x for x in [1])()()()
# print(e)
# print(type(e))

# f = FunctionType(x for x in [1])()
# print(f)
# print(type(f))

# g = FunctionType(x for x in [1])()()
# print(g)
# print(type(g))

# h = FunctionType(x for x in [1])()()()
# print(h)
# print(type(h))
