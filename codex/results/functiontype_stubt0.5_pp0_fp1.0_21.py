from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a))
print(type(b))

print(type(print))
print(type(FunctionType))
print(type(FunctionType) == type(type))
print(type(FunctionType) is type(type))

print(type(type))
print(type(type) == type(type))
print(type(type) is type(type))

print(type(type(type(type))))

print(type(type(type(type))) is type)

print(type(type) == type)
print(type(type) is type)

print(type(FunctionType) == type)
print(type(FunctionType) is type)


print('--------------------------------')
class A(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

a
