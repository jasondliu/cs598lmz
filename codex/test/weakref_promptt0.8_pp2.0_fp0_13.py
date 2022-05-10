import weakref
# Test weakref.ref()
import _weakref

def f(): pass

# Test weakref on a function
wr = weakref.ref(f)
assert wr() is f

# Test weakref on a special method
wr = weakref.ref(_weakref.__newobj__)
assert wr() is _weakref.__newobj__
wr = weakref.ref(_weakref.__init__)
assert wr() is _weakref.__init__

# Test weakref on a static method
class C:
    @staticmethod
    def g(): pass

wr = weakref.ref(C.g)
assert wr() is C.g

# Test weakref on a class method
class C:
    @classmethod
    def h(cls): pass

wr = weakref.ref(C.h)
assert wr() is C.h

# Test weakref on a builtin
import time
wr = weakref.ref(time.time)
assert wr() is time.time

# Test weakref on a module
import sys
wr = weakref.ref(sys)
