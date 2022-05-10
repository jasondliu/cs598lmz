from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(a == b)

def f():
    print('hello')
print(type(f))
print(type(FunctionType))
print(type(FunctionType) == type(f))

def f():
    pass

class A:
    pass

a = A()
print(type(f))
print(type(A))
print(type(a))
print(type(A) == type(a))
print(type(f) == FunctionType)
print(type(A) == type)
print(type(A) == type(type))
print(type(type(A)))
print(type(type(A)) == type)
print(type(type(A)) == type(type))

class A:
    def f(self):
        print('f')

a = A()
print(a.f)
print(type(a.f))
print(type(a.f) == FunctionType)
print(type(a.f) == type(f))

