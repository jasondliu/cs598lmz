import weakref
# Test weakref.ref and weakref.WeakKeyDictionary

from operator import eq
import gc

from support import gc_collect, gc_collect_harder

class A(object):
    def __init__(self):
        self.C = C(self)

class B(object):
    pass

class C(object):
    def __init__(self, parent):
        self.parent = weakref.ref(parent)

class Y(object):
    def __init__(self):
        self.D = D()


def cleanup():
    gc_collect_harder()
    supported = weakref.ReferenceType is not object
    if supported:
        UdefType = weakref.ReferenceType

        if not UdefType is object:
            # Manual cleanup
            gc_collect_harder()

            keys = []
            refs = []
            objs = []

            for o in gc.get_objects()[:]:
                if isinstance(o, UdefType) and safe_type(o):
                    refs.append(o)

