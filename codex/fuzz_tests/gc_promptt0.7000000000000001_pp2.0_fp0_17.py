import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.DEBUG_COLLECTABLE
#
# Here we test whether gc.collect() really calls tp_dealloc() for
# collectable objects and whether tp_dealloc() is called with the
# correct argument (the object's refcount == 0).

import gc
import weakref


class Collectable(object):
    def __init__(self):
        self.dealloc_called = False

    def __del__(self):
        if self.dealloc_called:
            raise Exception("__del__() already called")
        self.dealloc_called = True

        if self.dealloc_arg != 0:
            raise Exception("__del__(): expected arg == 0, got %d" %
                            self.dealloc_arg)

        if self.dealloc_obj is not self:
            raise Exception("__del__(): 'self' argument is incorrect")


class A(Collectable):
    pass

class B(Collectable):
    pass


def dealloc_hook(obj, arg):
    if not isinstance(obj, Collectable):
