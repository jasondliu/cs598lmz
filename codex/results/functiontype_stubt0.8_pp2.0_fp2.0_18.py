from types import FunctionType
a = (x for x in [1])
print(type(a))
a = [x for x in [1]]
print(type(a))
a = [x for x in [1] if x]
print(type(a))
