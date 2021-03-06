from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(next(a) == next(b))
print([1, 2] == [1, 2])
print(1 in [1, 2])
print(111 in [1, 2])
print(111 not in [1, 2])

print(isinstance(abs, FunctionType))
print(isinstance(lambda x: x, FunctionType))
print(isinstance(str.lower, FunctionType))
print(isinstance(str.lower, MethodType))
print(isinstance(str.lower, object))
print(isinstance(str.lower, (str, int, list)))

print(dir(1))
print(dir(None))
print(dir(list))
print(dir([1, 2]))
print(dir(tuple))
print(dir((1, 2)))
print(dir(dict))
print(dir({1, 2}))
print(dir(str))
print(dir('a'))
print(dir(int))
print(dir(float))
print(dir(
