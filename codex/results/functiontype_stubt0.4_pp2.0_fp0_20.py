from types import FunctionType
a = (x for x in [1])
print(type(a))

b = (x for x in [1])
print(type(b))

print(a == b)
print(a is b)
print(id(a) == id(b))

def f():
    print("hello world")

print(type(f))
print(type(f) == FunctionType)
print(type(f) is FunctionType)

print(isinstance(f, FunctionType))
print(isinstance(f, type))

print(type(FunctionType))
print(type(type))

print(type(FunctionType) == type)
print(type(FunctionType) is type)

print(isinstance(FunctionType, type))
print(isinstance(type, type))

# print(type(type))
# print(type(type) == type)
# print(type(type) is type)
#
# print(isinstance(type, type))
