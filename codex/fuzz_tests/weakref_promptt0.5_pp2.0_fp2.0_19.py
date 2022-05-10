import weakref
# Test weakref.ref()'s argument
def f():
    pass

class C:
    pass

class D(C):
    pass

print weakref.ref(f)
print weakref.ref(C)
print weakref.ref(D)
try:
    print weakref.ref(1)
except TypeError, e:
    print e

class E:
    pass

print weakref.ref(E())
try:
    print weakref.ref(E)
except TypeError, e:
    print e
