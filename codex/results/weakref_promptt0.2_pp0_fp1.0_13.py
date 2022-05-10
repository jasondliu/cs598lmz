import weakref
# Test weakref.ref(obj)

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.ref(a)     # create a weak reference to it
print(d)               # get the object if it is alive
print(d())             # get the object if it is alive

del a                  # remove the one reference
print(d)               # weak reference d still exists
print(d())             # d() returns None, because a is dead

print(d() is None)     # d() returns None, because a is dead
print(d() is None)     # d() returns None, because a is dead

print(d() is None)     # d() returns None, because a is dead
print(d() is None)     # d() returns None, because a is dead

print(d() is None)     # d() returns None, because a is dead
print(d() is None)     # d() returns None,
