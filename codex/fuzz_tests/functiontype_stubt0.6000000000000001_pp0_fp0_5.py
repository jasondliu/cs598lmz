from types import FunctionType
a = (x for x in [1])
b = [1, 2, 3]
c = {1, 2, 3}
d = {1:'a', 2:'b'}
e = FunctionType

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print(isinstance(b, list))
print(isinstance(c, set))
print(isinstance(d, dict))

print(isinstance(d, list))
print(isinstance(d, set))
print(isinstance(d, dict))

print(isinstance(d, (dict, set)))

print(dir(a))
print(dir(b))
print(dir(c))
print(dir(d))
print(dir(e))

print(len(dir(e)))
print(len(dir(d)))
print(len(dir(c)))
print(len(dir(b)))
print(len(dir(a)))

print(dir(a)[0])
print(dir(b)[0])
print(dir
