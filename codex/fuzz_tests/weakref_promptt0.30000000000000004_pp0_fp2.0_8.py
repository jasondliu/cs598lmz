import weakref
# Test weakref.ref() with a class instance.

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)

del o
print(r())

# Test weakref.ref() with a callable object.

class C:
    def __call__(self):
        return 42

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)

del o
print(r())

# Test weakref.ref() with a builtin function.

import sys

def f():
    pass

r = weakref.ref(f)
print(r)
print(r())
print(r() is f)

del f
print(r())

# Test weakref.ref() with a builtin method.

r = weakref.ref(sys.getrefcount)
print(r)
print(r())
print(r() is sys.getrefcount)

del sys

