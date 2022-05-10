import weakref
# Test weakref.ref

class Foo:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return 'Foo(%s)' % self.value

def callback(r):
    print('callback', r)

obj = Foo(42)
r = weakref.ref(obj, callback)
print('obj:', obj)
print('ref:', r)
print('r():', r())
print('deleting obj')
del obj
print('r():', r())
print('r():', r())

# Test weakref.WeakValueDictionary

d = weakref.WeakValueDictionary()
o1 = Foo(1)
d['1'] = o1
print(d['1'])
o2 = Foo(2)
d['2'] = o2
print(d['2'])
print(d['1'])
del o2
print(d.items())
print(d.items())
del o1
print(d.items())
