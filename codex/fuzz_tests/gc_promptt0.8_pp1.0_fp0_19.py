import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when a class has __del__ and
# weakref instances exist

class C:
    def __init__(self, arg):
        self.arg = arg
    def __del__(self):
        # save id, because it won't be available in gc callback
        self.id = id(self)
        C.n -= 1
        print "__del__", self
    def __repr__(self):
        return "C(%r)" % (self.arg,)


def create(n):
    global C_wr
    C.n = n
    C_wr = [None] * n
    for i in range(n):
        c = C(i)
        C_wr[i] = weakref.ref(c)
    del c

def check_results(n):
    print "dead:", gc.garbage
    l = gc.get_objects()
    print "live:", l
    assert len(l) == n
    for i in range(n):
        c = C_wr[i]()
        assert c
