from types import FunctionType
a = (x for x in [1])

# b = (x for x in [1])
# c = (x for x in [1])

# print(a is b is c)

# c_fn = c.__next__


# c_fn.__globals__['__builtins__'] = {}
# c_fn()


def x():
    pass
#print(type(x))
#print(type(x.__globals__))

b = (x for x in [1])
print(b.__next__.__globals__)
