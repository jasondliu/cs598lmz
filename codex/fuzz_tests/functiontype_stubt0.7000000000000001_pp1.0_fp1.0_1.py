from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])


def t():
    print('hi')

print(type(a))
print(type(b))
print(type(t))
print(isinstance(t, FunctionType))
print(isinstance(lambda x: x, FunctionType))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
