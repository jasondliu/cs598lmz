import weakref
# Test weakref.ref() on a class without a __del__ method.
# This should not crash, even if the referent has a __del__ method.

class C:
    def __del__(self):
        print("__del__")

c = C()
r = weakref.ref(c)
del c
print("before")
print(r())
print("after")
