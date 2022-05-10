import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect without the finalizers of weakrefs
gc.collect()
print "--- 2"

gc_collecting = []
class A:
    def __del__(self):
        print >> sys.stderr, "del"
        gc_collecting.append(self)
    def __repr__(self):
        return "A"

# test with __del__
a = A()
a_w = weakref.ref(a)
gc.collect()
assert a_w() is a
del a
gc.collect()
assert gc_collecting == [a_w()]
del a_w
gc.collect()
assert gc_collecting == []

# test with callbacks that references a
a = A()
a_w = weakref.ref(a, lambda x: None)
gc.collect()
assert a_w() is a
del a
gc.collect()
assert gc_collecting == [a_w()]
del a_w
gc.collect()
assert gc_collecting == []

# test with an additional strong reference
