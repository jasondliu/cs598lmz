import weakref
# Test weakref.ref
import weakref
import gc


class C:
    pass


o = C()
r = weakref.ref(o)
print(r)
print(r())
del o
gc.collect()
print(r())

###############################################################################
# Test weakref.finalize
import weakref
import gc


class C:
    pass


def callback(r):
    print('callback({})'.format(r))


o = C()
f = weakref.finalize(o, callback, o)
print(f.alive)
del o
print(f.alive)
gc.collect()
print(f.alive)
f()
print(f.alive)
