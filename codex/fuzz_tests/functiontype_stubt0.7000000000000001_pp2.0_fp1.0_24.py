from types import FunctionType
a = (x for x in [1])
b = FunctionType(lambda :None)
print(type(a))
print(type(b))
print(type(type(a)))
print(type(type(b)))
