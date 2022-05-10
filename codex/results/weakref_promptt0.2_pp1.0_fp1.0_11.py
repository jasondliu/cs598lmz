import weakref
# Test weakref.ref()

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.ref(a)     # create a weak reference to it
print(d())             # get the object if it is still alive
print(d() is a)
print(d() == a)
print(d() is None)
del a                  # remove the one reference
print(d() is None)

# Test weakref.WeakValueDictionary

d = weakref.WeakValueDictionary()
a = A(10)
d['primary'] = a           # does not create a reference
d['alias'] = a
print(d['primary'])
print(d['primary'] is a)
print(d['primary'] == a)
del a
print(d['primary'])
print(d['primary'] is None)
print(d['primary'] == None)

# Test weakref.WeakKeyDictionary

class B
