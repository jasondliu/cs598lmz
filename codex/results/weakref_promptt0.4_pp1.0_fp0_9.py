import weakref
# Test weakref.ref(x)

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.ref(a)     # create a weak reference to it
print(d())             # print 10
print(d() is a)        # print True
print(d() == a)        # print True

del a                  # remove the one reference
print(d() is None)     # print True

# Test weakref.proxy(x)

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.proxy(a)   # create a proxy to it
print(d)               # print 10
print(d is a)          # print True
print(d == a)          # print True

del a                  # remove the one reference
