import weakref
# Test weakref.ref() on a cyclic gc-enabled class.
class C:
    pass
test = C()
test.foo = test
wr = weakref.ref(test)
