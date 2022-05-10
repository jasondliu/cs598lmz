import weakref
# Test weakref.ref()

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.ref(a)     # create a weak reference to it
print(d())             # print the value through the reference
print(d() is a)        # the original object is still alive
print(d() == a)        # the original object is still alive
del a                  # remove the one reference
print(d() is None)     # now the weak reference gives None

# Test weakref.WeakValueDictionary

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a       # does not create a reference
d['secondary'] = a     # does not create a reference
print(d['primary
