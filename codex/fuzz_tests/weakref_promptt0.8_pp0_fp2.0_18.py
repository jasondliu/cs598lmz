import weakref
# Test weakref.ref
import builtins
import sys
import test.support

class C:
    deltas = []
    def __init__(self, label):
        self.label = label
    def __del__(self):
        self.deltas.append(self.label)

def f():
    pass

class D(object):
    def __del__(self):
        pass

def g():
    pass

class E(object):
    def __del__(self):
        pass

def h():
    pass

class F(object):
    """Class that is expected to be collected."""
    def __del__(self):
        """Mark the instance as collectable."""
        self.x = 1


@test.support.cpython_only
class ClearOnException(object):

    def __del__(self):
        """Delete the current context on deletion."""
        try:
            raise TypeError
        except:
            sys.exc_clear()

@test.support.cpython_only
class ClearOnExceptionInDel(object):


