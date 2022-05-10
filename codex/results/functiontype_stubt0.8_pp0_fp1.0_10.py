from types import FunctionType
a = (x for x in [1])
print(type(a))
print(a.__next__())

print(type(int.__new__))
print(type(type.__new__))
print(type(dict.__new__))
print(type(FunctionType.__new__))

print(type(int()))
print(type(type))
print(type(dict()))
print(type(FunctionType))
print(type(FunctionType(lambda x: None, globals())))
print(type(FunctionType(lambda x: None, globals(), "foo")))
print(type(FunctionType(lambda x: None, globals(), "foo", (1, 2))))
print(type(FunctionType(lambda x: None, globals(), "foo", (1, 2), {"bar": 1})))

b = type(lambda: None)
print(type(b))
