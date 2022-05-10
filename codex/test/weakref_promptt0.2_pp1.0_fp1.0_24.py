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
a = None               # remove the one reference
print(d)               # d is dead
print(d())             # d is dead

# Test weakref.WeakKeyDictionary

class B:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

b1 = B(10)
b2 = B(20)
b3 = B(30)

d = weakref.WeakKeyDictionary()
d[b1] = 'b1'
d[b2] = 'b2'
d[b3] = 'b3'
