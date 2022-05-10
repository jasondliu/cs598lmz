import weakref
# Test weakref.ref() on a method
class C:
    def m(self):
        pass

obj = C()
r = weakref.ref(obj.m)
assert r() is obj.m
del obj
assert r() is None

# Test weakref.ref() on a builtin method
import operator
r = weakref.ref(operator.add)
assert r() is operator.add
assert r()(1, 2) == 3
del operator
assert r() is None

# Test weakref.ref() on a builtin function
import operator
r = weakref.ref(operator.abs)
assert r() is operator.abs
assert r()(-1) == 1
del operator
assert r() is None

# Test weakref.ref() on a builtin function
import operator
r = weakref.ref(operator.index)
assert r() is operator.index
assert r()(1) == 1
del operator
assert r() is None

# Test weakref.ref() on a builtin method
import operator
r = weakref.ref(operator.index.__get__(1))
