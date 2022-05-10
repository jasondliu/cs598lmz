from types import FunctionType
a = (x for x in [1])
b = [1,2,3]
def f():
    pass


print(isinstance(a,FunctionType))
print(isinstance(b,FunctionType))
print(isinstance(f,FunctionType))

print(type(a))
print(type(b))
print(type(f))
