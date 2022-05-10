import weakref
# Test weakref.ref()

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.ref(a)     # create a weak reference to it
print(d())             # print the value via the reference
print(d() is a)        # reference objects compare like the objects they reference
print(d() == a)
print(d() is None)     # a is still alive, so the weak reference is not None

del a                  # remove the one reference to the object
print(d() is None)     # now the weak reference is None

print(d() is None)     # the weak reference is still None

# Test weakref.WeakValueDictionary

d = weakref.WeakValueDictionary()
o = A(10)
d['primary'] = o
print(d['primary'])

del o
print(d['primary'])

# Test weakref.WeakKeyDictionary

d = weakref
