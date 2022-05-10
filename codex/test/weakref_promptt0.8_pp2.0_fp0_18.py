import weakref
# Test weakref.ref when the referent is a class.


class TestClass:
    pass


A = TestClass()
id_A = id(A)
r = weakref.ref(A)
del A
if r() is not None:
    raise Exception("weakref not working properly")

B = TestClass()
id_B = id(B)
if id_A != id_B:
    raise Exception("debug allocator this time")

t = TestClass()
id_t = id(t)
r = weakref.ref(t)
del t
if r() is not None:
    raise Exception("weakref not working properly")

t = TestClass()
if id_t != id(t):
    raise Exception("debug allocator this time")

t = TestClass()
id_t = id(t)
r = weakref.ref(t)
del t

if r() is not None:
    raise Exception("weakref not working properly")

t = TestClass()
if id_t != id(t):
    raise Exception("debug allocator this time")
