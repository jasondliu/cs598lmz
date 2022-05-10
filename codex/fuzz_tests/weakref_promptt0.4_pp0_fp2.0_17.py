import weakref
# Test weakref.ref() and weakref.proxy() with a class instance.

class C:
    pass

o = C()
r = weakref.ref(o)
p = weakref.proxy(o)

print(r(), p)

del o

print(r(), p)

try:
    print(r())
except ReferenceError:
    print("ReferenceError")

try:
    print(p)
except ReferenceError:
    print("ReferenceError")
