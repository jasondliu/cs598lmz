import weakref
# Test weakref.ref()

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.ref(a)     # create a weak reference to a
print(d)               # print the weak reference
print(d())             # dereference the weak reference
print(d() is a)        # verify that d() is a
print(d() == 10)       # verify that d() is 10

del a                  # delete the reference
print(d())             # d() is still 10
print(d() is None)     # but d() is now dead

a = A(10)              # create a reference
d = weakref.ref(a)     # create a weak reference to a
print(d)               # print the weak reference
print(d())             # dereference the weak reference
print(d() is a)        # verify that d() is a
print(d() == 10)       # verify that d() is 10

a
