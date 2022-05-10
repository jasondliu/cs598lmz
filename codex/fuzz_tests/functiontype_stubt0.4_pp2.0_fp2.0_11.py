from types import FunctionType
a = (x for x in [1])
print(type(a))

b = FunctionType(a, globals(), None, None, None)
print(type(b))
print(b)

print(b())

#print(b())

#print(b())

#print(b())
