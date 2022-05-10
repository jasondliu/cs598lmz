import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc, latefin

gc.collect()
assert callable(func), func

from gc import _pod_unreachable
from weakref import ReferenceType

class C(object):
    pass

def check_pod_unreachable():
    lst = _pod_unreachable()
    if not lst:
        print "no unreachable objects"
        return

    for item, refs in lst:
        print "found %d unreachable %s objects" % (len(item), type(item))
        for i, ref in enumerate(refs):
            typ = type(ref)
            ref = repr(ref)
            if isinstance(typ, type):
                ref = '%s %s' % (typ.__name__, ref)
            else:
                ref = '%s %s' % (type(typ), ref)
            print '    ', i + 1, ':', ref
        print

c = C()
c.foo = ReferenceType(c)
ref = ReferenceType(c)
c.bar = ref
w1 =
