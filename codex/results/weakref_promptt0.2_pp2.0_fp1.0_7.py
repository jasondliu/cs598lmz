import weakref
# Test weakref.ref(obj)

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.ref(a)     # create a weak reference to it
print(d())             # get the object if it is still alive
print(d() is a)
del a                  # remove the one reference
print(d())             # the object was destroyed
print(d() is None)

# Test weakref.getweakrefcount(object)

a = A(10)
d = weakref.ref(a)
print(weakref.getweakrefcount(a))

# Test weakref.getweakrefs(object)

a = A(10)
d = weakref.ref(a)
print(weakref.getweakrefs(a))

# Test weakref.proxy(object[, callback])

a = A(10)
p = weakref.proxy(a)
print(p.value
