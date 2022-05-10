import gc, weakref, copy, os, time
import unittest
import tempfile, shutil
from compat import u, b
try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO
import six

def test_rr_registers_trees_and_references():
    t1 = []
    t2 = [t1]
    weak_t2 = weakref.ref(t2)
    assert weak_t2() is t2
    t1.append(t2)
    del t1, t2

    gc.collect()

    assert weak_t2() is None

def test_rr_recycler_does_not_collect_the_wrong_references():
    import weakref
    def subtypes(cls):
        return [cls] + [b for a in cls.__subclasses__()
                           for b in subtypes(a)]

    to_finalize = []
    to_extristicate = []
    class Recycled(object):
        pass

    class Recycler(Recycled
