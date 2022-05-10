import weakref
# Test weakref.ref()
def foo(x):
    print('foo')
    return x

x = foo(42)
r = weakref.ref(x, foo)

print(r)
print(r())

x = None
print(r())

# Test weakref.WeakKeyDictionary
class Foo(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Foo %s>' % self.name

def bar(self):
    print(self.name)

f1 = Foo('f1')
f2 = Foo('f2')

d = weakref.WeakKeyDictionary()
d[f1] = bar
d[f2] = bar

print(d[f1])
print(d[f2])

f1 = None
print(d)

f2 = None
print(d)

# Test weakref.WeakValueDictionary
class Foo(object):
    def __init__(self, name):
        self.name = name


