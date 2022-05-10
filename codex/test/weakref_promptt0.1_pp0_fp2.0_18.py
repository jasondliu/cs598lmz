import weakref
# Test weakref.ref()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def callback(r):
    print('callback(', r, ')')

f = Foo('f')
r = weakref.ref(f, callback)
print('created:', r)
print('f:', f)
print('r():', r())
print('deleting f')
del f
print('r():', r())

# Test weakref.WeakKeyDictionary

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

d = weakref.WeakKeyDictionary()
f1 = Foo('f1')
f2 = Foo('f2')
d[f1] = 1
d[f2] = 2
print(d.items())
del f1
print(d.items())

#
