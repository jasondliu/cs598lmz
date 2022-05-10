import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref
def callback(ref):
    print "callback()"
    print "ref:", ref
    print "ref():", ref()
    print

class C:
    def __del__(self):
        print "C.__del__"

def test():
    c = C()
    c.x = c
    wr = weakref.ref(c, callback)
    print "created ref:", wr
    print "ref():", wr()
    print
    del c
    print "deleted c"
    print "ref:", wr
    print "ref():", wr()
    print
    gc.collect()

test()

print "all done"
