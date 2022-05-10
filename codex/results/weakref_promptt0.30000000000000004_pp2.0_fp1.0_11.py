import weakref
# Test weakref.ref
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)             # create a reference
d = weakref.ref(a)     # create a weak reference to a
print(d())            # get a
print(d() is a)
print(d() == a)
a = A(12)             # change the value of a
print(d())            # get the new value of a via the weak reference
print(d() is a)
print(d() == a)
del a                 # delete the reference
print(d())            # d is still alive because a is still alive
print(d() is a)
print(d() == a)
del d                 # delete the weak reference
#print(d())            # d is dead
#print(d() is a)
#print(d() == a)

# Test weakref.WeakValueDictionary
d = weakref.WeakValueDictionary()
a = A(10)
d['primary
