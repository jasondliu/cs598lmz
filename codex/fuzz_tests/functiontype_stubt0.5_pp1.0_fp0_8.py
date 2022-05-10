from types import FunctionType
a = (x for x in [1])
b = [1]
print(type(a))
print(type(b))

def f():
    pass

print(type(f))
print(type(f) == FunctionType)

print(type(lambda x: x))
print(type(lambda x: x) == FunctionType)

print(type(abs))
print(type(abs) == FunctionType)

print(type(int))
print(type(int) == FunctionType)

print(type(max))
print(type(max) == FunctionType)

print(type(range))
print(type(range) == FunctionType)

print(type(dict))
print(type(dict) == FunctionType)

print(type(list))
print(type(list) == FunctionType)

print(type(tuple))
print(type(tuple) == FunctionType)

print(type(set))
print(type(set) == FunctionType)
