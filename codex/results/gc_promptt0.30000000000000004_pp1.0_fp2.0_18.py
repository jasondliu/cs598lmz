import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.

def callback(wr):
    print "callback:", wr, wr()

class C:
    def __init__(self, n):
        self.n = n
    def __repr__(self):
        return "<C %s>" % self.n

def test(n):
    c = C(n)
    wr = weakref.ref(c, callback)
    print "created:", wr, wr()
    del c
    gc.collect()
    print "collected:", wr, wr()

test(1)
test(2)
test(3)
test(4)
test(5)
test(6)
test(7)
test(8)
test(9)
test(10)
test(11)
test(12)
test(13)
test(14)
test(15)
test(16)
test(17)
test(18)
test(19)
test(20)
test(21)
test(22)
test(23)
test(24)
test
