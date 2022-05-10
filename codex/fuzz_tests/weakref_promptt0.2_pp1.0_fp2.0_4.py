import weakref
# Test weakref.ref()

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def callback(r):
    print 'callback(', r, ')'

a = Foo('a')
d = weakref.WeakValueDictionary()
d['primary'] = a
r = weakref.ref(a, callback)
print 'before:', r, d.keys()
del a
print 'after:', r, d.keys()

print 'r():', r()
print 'd["primary"]:', d['primary']

print 'd.items():', d.items()

print 'd.values():', d.values()

print 'd.get("primary"):', d.get('primary')

print 'd.get("primary", "n/a"):', d.get('primary', 'n/a')

print 'd.get("foo", "n/a"):', d.get('foo', 'n/a')
