import weakref
# Test weakref.ref() works.

class A:
    pass

a = A()

# weakref to an instance
r1 = weakref.ref(a)
assert r1() is a

# weakref to a class
r2 = weakref.ref(A)
assert r2() is A

# weakref to a function
r3 = weakref.ref(A.__init__)
assert r3() is A.__init__

# weakref to a module
import sys
r4 = weakref.ref(sys)
assert r4() is sys

# weakref to a method
r5 = weakref.ref(a.__eq__)
assert r5() is A.__eq__

# weakref to an instance method
r6 = weakref.ref(a.__hash__)
assert r6() is A.__hash__

# weakref to a builtin
import gc
r7 = weakref.ref(gc.collect)
assert r7() is gc.collect

# weakref to a builtin method
r8 = weakref.ref
