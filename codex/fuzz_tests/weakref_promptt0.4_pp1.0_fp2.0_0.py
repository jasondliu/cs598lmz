import weakref
# Test weakref.ref()
class A:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'A(%s)' % self.x

a = A(10)              # create a reference
d = weakref.ref(a)     # create a weak reference to it
print(d())             # get the object if it is still alive
del a                  # remove the one reference
print(d())             # d is dead

a = A(10)
d = weakref.ref(a)
print(d())
a = None
print(d())

# Test weakref.WeakValueDictionary
class A:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'A(%s)' % self.x

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
del a
print(d['primary'])

a = A(10)
d =
