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
del func, cyc

gc.collect()


class Dummy:
    pass

class Discarder:
    def __getattribute__(self, attr):
        self.attr = attr
        return self
    def __call__(self, *args, **kwargs):
        return Dummy()

d = Discarder()

# Attributes of deleted instances should be discarded by the
# GC.  In order to ensure the GC is run, we need a new reference cycle
# each time.  We create the cycle by creating a C object and then
# throwing away all references to it.
class C:
    pass

# Create a new reference cycle and discard all references to it.
def new_cycle():
    o = C()
    o.x = o

def test_discard():
    # Generate reference cycles until no more can be generated.
    # Then verify that the attribute which was supposed to be discarded
    # is no longer present.
    while 1:
        try:
            new_cycle()
        except RecursionError:
            break
    try:
        d.x
