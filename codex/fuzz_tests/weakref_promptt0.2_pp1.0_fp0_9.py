import weakref
# Test weakref.ref()

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
print(d() is None)
print(d() == None)
print(d() is not None)
print(d() != None)
print(d() is not a)
print(d() != a)

del a                  # remove the one reference
print(d() is None)
print(d() == None)
print(d() is not None)
print(d() != None)

try:
    print(d())
except ReferenceError:
    print("ReferenceError")

try:
    print(d() is None)
except ReferenceError:
    print("ReferenceError")

try:
    print(d()
