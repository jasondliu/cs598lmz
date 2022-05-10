import weakref
# Test weakref.ref()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def callback(r):
    print('callback(', r, ')')

a = Foo('a')
d = weakref.WeakValueDictionary()
d['primary'] = a
r = weakref.ref(a, callback)
print('r:', r)
print('d:', d)
a = None
print('d:', d)

# Test weakref.proxy()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

a = Foo('a')
p = weakref.proxy(a)
print('p:', p)
print('p.name:', p.name)
a = None
print('p.name:', end=' ')
print(p.name)
