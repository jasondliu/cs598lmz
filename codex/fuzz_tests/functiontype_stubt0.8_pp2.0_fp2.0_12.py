from types import FunctionType
a = (x for x in [1])
print(a.__name__)

print(FunctionType.__name__)
print(lambda x : x)
