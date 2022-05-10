import types
types.SimpleNamespace

#%%
import types

class A:
    pass

def foo(self):
    print('foo')

a = A()

a.foo = types.MethodType(foo, a)

a.foo()

#%%
class A:
    def __init__(self):
        self.a = 1
        self.b = 2

a = A()

print(a.__dict__)
print(a.a)
print(a.b)

#%%
class A:
    def __init__(self):
        self.a = 1
        self.b = 2

a = A()

a.c = 3

print(a.__dict__)
print(a.a)
print(a.b)
print(a.c)

#%%
class A:
    def __init__(self):
        self.a = 1
        self.b = 2

a = A()

a.c = 3

print(a.__dict__)
print(a.a)
