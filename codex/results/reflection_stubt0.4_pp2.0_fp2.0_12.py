fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #12092: crash when __code__ is set to a non-code object.
import types
class A(object):
    def __init__(self):
        self.__code__ = None
class B(object):
    def __init__(self):
        self.__code__ = A()
class C(object):
    def __init__(self):
        self.__code__ = types.FunctionType(A(), {})

# Issue #12093: crash when __code__ is set to a code object with a NULL co_zombieframe
import types
def f(): pass
f.__code__ = types.FunctionType(f.__code__, {}).__code__

# Issue #12094: crash when __code__ is set to a code object with a NULL co_zombieframe
# and a non-NULL co_weakreflist
import types
def f(): pass
f.__code__ = types.FunctionType(f.__code__, {}).__code__
import weakref
weakref.ref(
