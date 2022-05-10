import weakref
# Test weakref.ref

class C:
    pass

o = C()
r = weakref.ref(o)
if r() is not o:
    raise TestFailed, "weakref.ref() did not return original object"

del o
if r() is not None:
    raise TestFailed, "weakref.ref() did not return None"

# Test weakref.proxy

class C:
    pass

o = C()
p = weakref.proxy(o)
if p is not o:
    raise TestFailed, "weakref.proxy() did not return original object"

del o
try:
    p.foo
except ReferenceError:
    pass
else:
    raise TestFailed, "weakref.proxy() did not raise ReferenceError"


# Test that a weakref can be created to an object with a __del__ method
class C:
    def __del__(self):
        pass

o = C()
r = weakref.ref(o)
if r() is not o:
    raise TestFailed, "weakref.ref() did
