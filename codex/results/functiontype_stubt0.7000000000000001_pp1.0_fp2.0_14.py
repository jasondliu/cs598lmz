from types import FunctionType
a = (x for x in [1])
print(type(a))

def f():
    pass
f.__name__ = 'f'
print(type(f))
print(f.__name__)
print(type(FunctionType))

print(dir(f))
# print(dir(FunctionType))

class A():
    def __init__(self):
        pass
    def __call__(self):
        print('__call__')
print(type(A))
a = A()
print(type(a))
a()
print(dir(A))
print(dir(a))
