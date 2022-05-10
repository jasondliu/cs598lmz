import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect(): cyclic garbage is collectable
# when the generation is big enough.
c = weakref.WeakValueDictionary()
d = weakref.WeakValueDictionary()
class Foo:
    pass
o = Foo()
c['1'] = o
c['2'] = o
del o
import gc
gc.collect()
# This shouldn't throw RuntimeError, since o was collected
"1" in c
"2" in d
class Bar(object):
    pass
# Test gc.collect(): cyclic garbage is collectable
# when the generation is big enough.
c = {1: object()}
d = {2: []}
o = Bar()
c[3] = o
d[4] = o
del o, c, d
import gc
gc.collect()


# Test gc.collect(): cyclic garbage is collectable
# when the generation is big enough.
c = {1: object()}
d = {}
o = Bar()
c[3] = o
d[o] = 1
b = []
b.append(b)
del o
