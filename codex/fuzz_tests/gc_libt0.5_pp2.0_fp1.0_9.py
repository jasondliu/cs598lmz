import gc, weakref

class C(object):
    pass

c = C()

def on_del(wr, name):
    print "on_del", name

weakref.finalize(c, on_del, "c")

print "del c"
del c

print "gc.collect()"
gc.collect()

print "done"
