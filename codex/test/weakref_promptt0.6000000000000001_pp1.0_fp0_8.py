import weakref
# Test weakref.ref
def f(x):
    return lambda n: print(x(n))

class A:
    def __init__(self, name):
        self.name = name
    def __call__(self, n):
        return 'A(' + str(n) + ').' + self.name

a = A('a')

b = f(a)
b(0)
del a
b(1)

# Test weakref.proxy
class B:
    def __init__(self, name):
        self.name = name
    def __call__(self, n):
        return 'B(' + str(n) + ').' + self.name

b = B('b')

c = weakref.proxy(b)
c(0)
del b
try:
    c(1)
except ReferenceError:
    pass
else:
    print('ReferenceError expected')
