import weakref
# Test weakref.ref()

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.ref(a)     # create a weak reference to a
print(d())             # print 10
print(d() is a)        # print True
print(d() == a)        # print True

del a                  # remove the one reference
print(d() is None)     # print True
print(d() == None)     # print True

# Test weakref.WeakValueDictionary()

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a       # does not create a reference
d['primary']           # fetch the object if it is still alive
del a                  # remove the
