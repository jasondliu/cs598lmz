import weakref
# Test weakref.ref
class C:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(' + self.name + ')'

c = C('name')
r = weakref.ref(c)
print(r())
print(r() is c)
del c
print(r())

# Test weakref.WeakValueDictionary
d = weakref.WeakValueDictionary()
d['primary'] = c
print(d['primary'])
del c
print(d['primary'])

# Test weakref.WeakKeyDictionary
d = weakref.WeakKeyDictionary()
d[c] = 'value'
print(d[c])
del c
try:
    print(d[c])
except KeyError:
    print('KeyError')

# Test weakref.WeakSet
s = weakref.WeakSet()
s.add(c)
print(s)
del c
print(s)

# Test weakref.finalize
class C:
    def __init__(self
