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
print(d() == a)
del a                  # remove the one reference
print(d())             # d is dead
print(d() is None)

# Test weakref.ref(obj, callback)

def callback(x):
    print('callback({!r})'.format(x))

a = A(10)
d = weakref.ref(a, callback)
print(d())
del a
print(d())

# Test weakref.WeakKeyDictionary

class Cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(self):
        return 'Cheese(%r)'
