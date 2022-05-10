import weakref
# Test weakref.ref(C())
class C:
    def __init__(self):
        self.c = 1
    def __del__(self):
        print("C.__del__")

d = weakref.ref(C())
print(d(), d().c)
d().c = 2
print(d(), d().c)
del d().c
print(d(), d().c)
del d()
print(d())

# Test weakref.ref(C()) where C has a __del__ method that raises an exception
class C:
    def __del__(self):
        print("C.__del__")
        raise Exception

try:
    d = weakref.ref(C())
except Exception:
    print("Caught an exception")

# Test weakref.ref(C()) where C has a __del__ method that raises an exception
# and has a __weakref__ slot
class C:
    __slots__ = ['__weakref__', 'c']
    def __init__(self):
        self.c = 1
    def __del__(self
