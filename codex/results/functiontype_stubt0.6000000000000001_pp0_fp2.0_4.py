from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
print(type(a))
print(type(b))
print(type(int))
print(type(str))
print(type(list))
print(type(dict))
print(type(FunctionType))
