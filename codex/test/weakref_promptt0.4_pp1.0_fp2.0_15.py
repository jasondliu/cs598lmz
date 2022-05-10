import weakref
# Test weakref.ref()

class Foo:
    def __init__(self):
        self.data = 42

f = Foo()

r = weakref.ref(f)
print(r())

f = None
print(r())

print(r() is None)

# Test weakref.WeakKeyDictionary

class Foo:
    def __init__(self):
        self.data = 42

f = Foo()

d = weakref.WeakKeyDictionary()
d[f] = 'bar'
print(d[f])

f = None
try:
    print(d[f])
except KeyError:
    print('KeyError')

print(f in d)

# Test weakref.WeakValueDictionary

class Foo:
    def __init__(self):
        self.data = 42

f = Foo()

d = weakref.WeakValueDictionary()
d['foo'] = f
print(d['foo'].data)

f = None
