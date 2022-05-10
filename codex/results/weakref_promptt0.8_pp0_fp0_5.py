import weakref
# Test weakref.ref
def f(x):
    return x
foo = lambda x:x
x = weakref.ref(f)(foo)
print x

# Test weakref.proxy
class T(int):
    def __init__(self, value):
        self.value = value
    def x(self):
        return self.value

a = T(42)
y = weakref.proxy(a)
print y.x()

# Test dictionary
d = {'a':1,'b':2,'c':3}
weakref.proxy(d)
print weakref.proxy(d)['b']

# Test list
foo = [42]
z = weakref.proxy(foo)
if len(z) != 1: raise ValueError
if z[0] != 42: raise ValueError

# Test set
a1 = set([1,2,3])
y1 = weakref.proxy(a1)
if len(y1) != 3: raise ValueError

# Test frozenset
a2 = frozenset([1,2,3,4])
y
