import weakref
# Test weakref.ref() for callable objects.

class C(object):
    def __call__(self, *args):
        pass

obj = C()
r = weakref.ref(obj)

# calling the referent should not decref it
obj()
assert r() is obj

# calling the reference should invoke the referent
r()
assert r() is obj

# calling a dead reference should fail
assert r() is None
try:
    r()
except ReferenceError:
    pass
else:
    assert False, "calling dead reference didn't raise ReferenceError"
