import weakref
# Test weakref.ref() on a class with a __del__ method.

class C:
    def __del__(self):
        pass

r = weakref.ref(C())
print(r)
print(r())
