import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
print gc.collect() == 0

class Foo:
    def __init__(self):
        self.x = "test"

f = Foo()
f.__dict__['foo'] = 1

f_weak_ref = weakref.ref(f)
f_id = id(f)
print f_id in gc.garbage
print gc.is_tracked(f)

assert f_weak_ref() is f

del f
print f_id in gc.garbage
assert gc.collect() == 1, gc.collect()
print f_id in gc.garbage
print gc.is_tracked(f_id)

print gc.collect() == 0
gc.garbage.append(123)
print 123 in gc.garbage
assert gc.collect() == 1

assert f_weak_ref() is None

del f_weak_ref
print f_id in gc.garbage # weakref to f should be gone
print gc.is_tracked(f_id)


