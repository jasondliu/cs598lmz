import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to an object with a __del__ method with cyclic gc.
# Also tests their interaction with threading.

from test.support import run_with_tz
from test.support import threading_helper


class CycleWithDel(object):

    def __init__(self):
        self.bar = self

    def __del__(self):
        pass

class Foo(object):

    def __init__(self, target=None):
        self.target = target
        self.bar = target

    def __del__(self):
        pass

class Bar(object):

    def __init__(self, target=None):
        self.target = target
        if target:
            self.foo = target.foo

    def bar(self):
        return self

    def __del__(self):
        pass

def schedule():
    # Schedule a callback whose only purpose is to create a reference cycle.
    def foo(obj1, obj2):
        """doc string"""
        l = [obj1]
        l.append(l)

