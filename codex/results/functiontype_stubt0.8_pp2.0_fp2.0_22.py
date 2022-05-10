from types import FunctionType
a = (x for x in [1])
b = a.__iter__
c = a.__next__
print(isinstance(a, GeneratorType))
print(type(a))
print(isinstance(b, FunctionType))
print(type(b))
print(isinstance(c, FunctionType))
print(type(c))

# int, str, list, tuple, set, dict, function, module, class, type, none
# print(dir(str))
# print(dir(list))
print(dir(tuple))
print(dir(dict))
print(dir(dict))
print(dir(dict))
print(dir(dict))
print(dir(dict))
print(dir(dict))
print(dir(dict))
print(dir(dict))
print(dir(dict))
print(dir(dict))
print(dir(dict))
print(dir(dict))
