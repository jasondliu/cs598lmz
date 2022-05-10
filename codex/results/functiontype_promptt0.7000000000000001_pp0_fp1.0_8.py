import types
# Test types.FunctionType
def f1():
    pass
def f2(a, b):
    return a + b


t1 = types.FunctionType(f1.__code__, globals())
print(t1())

t2 = types.FunctionType(f2.__code__, globals(), 'foo', (1,2), None)
print(t2(3, 4))

print(t2.__name__)
print(t2.__defaults__)
print(t2.__closure__)
print(t2.__code__)
print(t2.__dict__)
print(t2.__doc__)
print(t2.__globals__)
print(t2.__module__)

# Test types.MethodType
class C:
    pass

c = C()
print(c.__class__)


def func(self):
    return 'called func'

c.func = types.MethodType(func, c)
print(c.func())

c2 = C()
print(c2.func())
