import weakref
# Test weakref.ref

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
print('d.data:', list(d.data.items()))
print('d.weakvalues:', list(d.weakvalues()))
print('d.items:', list(d.items()))
print('d.keys:', list(d.keys()))
print('d.values:', list(d.values()))
print('d.get:', d.get('primary'))
print('d.pop:', d.pop('primary'))
print('d:', d)
print('r:', r)
