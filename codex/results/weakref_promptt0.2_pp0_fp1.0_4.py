import weakref
# Test weakref.ref()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def callback(r):
    print('callback(', r, ')')

a = Foo('a')
d = weakref.WeakValueDictionary()
d['primary'] = a
r = weakref.ref(a, callback)
print('r:', r)
print('d:', d)
print('d["primary"]:', d['primary'])
print('r():', r())
print('deleting a')
del a
print('r():', r())
print('d["primary"]:', d['primary'])
print('d:', d)

# Test weakref.proxy()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

a = Foo('a')
p = weakref.proxy
