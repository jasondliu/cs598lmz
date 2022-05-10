import weakref
# Test weakref.ref()

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.ref(a)     # create a weak reference to it
print(d())             # check that it is working
del a                  # delete the reference
print(d())             # object has been garbage collected

# Test weakref.WeakKeyDictionary

class B:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = B(10)
b = B(20)
d = weakref.WeakKeyDictionary()
d[a] = 1
d[b] = 2
print(d[a])
del a
print(d[b])

# Test weakref.WeakValueDictionary

class C:
    def __init__(self, value):
        self.value = value
    def __re
