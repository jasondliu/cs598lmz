import weakref
# Test weakref.ref() on a function.

def f():
    pass

r = weakref.ref(f)
print(r())

del f
print(r())

# Test weakref.ref() on a built-in function.
r = weakref.ref(len)
print(r())

# Test weakref.ref() on a built-in method.
r = weakref.ref("".join)
print(r())

# Test weakref.ref() on a class.
class C:
    pass

r = weakref.ref(C)
print(r())

del C
print(r())

# Test weakref.ref() on a class instance.
class D:
    pass

d = D()
r = weakref.ref(d)
print(r())

del d
print(r())

# Test weakref.ref() on a generator function.
def g():
    yield 1

r = weakref.ref(g)
print(r())

del g
print(r())

# Test weakref.ref() on a
