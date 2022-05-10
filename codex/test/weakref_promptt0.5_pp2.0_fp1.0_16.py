import weakref
# Test weakref.ref() with a function
def f():
    pass
wr = weakref.ref(f)
assert wr() is f
# Test weakref.ref() with a method
class C:
    def m(self):
        pass
obj = C()
wr = weakref.ref(obj.m)
assert wr() is obj.m
# Test weakref.ref() with a builtin method
wr = weakref.ref(C.m)
assert wr() is C.m
# Test weakref.ref() with a builtin function
wr = weakref.ref(len)
assert wr() is len
# Test weakref.ref() with a class
wr = weakref.ref(C)
assert wr() is C
# Test weakref.ref() with a module
import sys
wr = weakref.ref(sys)
assert wr() is sys
# Test weakref.ref() with a builtin
wr = weakref.ref(int)
assert wr() is int
# Test weakref.ref() with a slice
wr = weakref.ref(slice(1, 2, 3))
assert wr()
