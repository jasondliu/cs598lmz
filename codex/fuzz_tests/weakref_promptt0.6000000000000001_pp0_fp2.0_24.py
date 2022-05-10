import weakref
# Test weakref.ref
import sys

class MyClass:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%s)' % self.name

o = MyClass('instance')
r = weakref.ref(o)
print(r())
print(r() is o)
o2 = MyClass('instance2')
r2 = weakref.ref(o2)
print(r2())
print(r2() is o2)

a = MyClass('a')
d = weakref.WeakValueDictionary()
d['primary'] = a
d['secondary'] = a
print(d['primary'])
print(d['secondary'])
print(d['primary'] is d['secondary'])

# Test weakref.WeakValueDictionary
a = MyClass('a')
d = weakref.WeakValueDictionary()
d['primary'] = a
d['secondary'] = a
print(d['primary'])
print(d['secondary'])
print(d['primary'] is d['secondary
