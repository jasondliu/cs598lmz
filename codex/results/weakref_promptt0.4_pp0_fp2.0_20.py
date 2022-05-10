import weakref
# Test weakref.ref()

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.ref(a)     # create a weak reference to it
print a, d()           # prints "10 10"
del a                  # remove the one reference
print d()              # prints "None"
print d() is None      # prints "True"
print

# Test weakref.WeakKeyDictionary and weakref.WeakValueDictionary

d = weakref.WeakKeyDictionary()
e = weakref.WeakValueDictionary()
a = A(10)
d[a] = 1
e[1] = a
print d[a], e[1]           # prints "1 10"
del a
print d, e                 # prints "{} {}"
print

# Test weakref.WeakSet

s = weakref.WeakSet()
a = A(10)
s.add(a)
print a in s
