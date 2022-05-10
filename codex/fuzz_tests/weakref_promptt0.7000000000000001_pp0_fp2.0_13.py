import weakref
# Test weakref.ref() on a cyclic gc-enabled class.
class C:
    pass
test = C()
test.foo = test
wr = weakref.ref(test)
print wr
del test
print wr
print wr() is None
# Test weakref.ref() on a cyclic gc-disabled class.
class C:
    __slots__ = ['foo']
test = C()
test.foo = test
wr = weakref.ref(test)
print wr
del test
print wr
print wr() is None
# Test weakref.ref() on a class with a __del__.
# This used to segfault.
class C:
    __slots__ = ['foo']
    def __del__(self):
        pass
test = C()
test.foo = test
wr = weakref.ref(test)
print wr
del test
print wr
print wr() is None
# Test weakref.ref() on a class with a weakrefable cyclic reference.
class C:
    __slots__ = ['foo']
class D:
    __slots__
