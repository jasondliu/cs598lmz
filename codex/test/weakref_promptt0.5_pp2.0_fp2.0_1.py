import weakref
# Test weakref.ref
#
import gc

class Dummy:
    pass

a = Dummy()
b = Dummy()

w = weakref.ref(a)

