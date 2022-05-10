import weakref
# Test weakref.ref() and weakref.proxy()

# Create a class with a __del__ method
class C:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print("del", self.name)

# Create a reference to an object
c = C("c")
r = weakref.ref(c)
print("ref", r)
print("ref", r())
print("ref", r.__call__())
print("ref", r.__call__().name)

# Create a proxy to an object
c = C("c")
p = weakref.proxy(c)
print("proxy", p)
print("proxy", p.name)

# Create a proxy to an object that doesn't exist
c = C("c")
r = weakref.ref(c)
del c
try:
    p = weakref.proxy(r())
except TypeError:
    print("TypeError")

# Create a proxy to an object that doesn't exist
c = C("c")
r = weakref.ref(c)
