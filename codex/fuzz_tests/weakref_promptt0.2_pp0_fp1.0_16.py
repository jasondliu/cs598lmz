import weakref
# Test weakref.ref()

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.ref(a)     # create a weak reference to it
print(d)               # get the object if it is alive
print(d())             # get the object if it is alive
print(d() is a)        # get the object if it is alive
del a                  # remove the one reference
print(d)               # weak reference is still alive
print(d() is None)     # but refers to dead object
print(d() is a)        # but refers to dead object

# Test weakref.WeakValueDictionary

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a      
