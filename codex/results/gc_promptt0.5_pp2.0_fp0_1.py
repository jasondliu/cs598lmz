import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage
class Test:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Test(' + self.name + ')'

def f():
    x = Test('f')
    y = Test('g')
    z = Test('h')
    t = Test('i')
    x.y = y
    y.x = x
    x.z = z
    y.z = z
    z.x = x
    z.y = y
    x.t = t
    y.t = t
    z.t = t
    t.x = x
    t.y = y
    t.z = z
    return x

def check(name, gc_enabled, garbage):
    print('gc_enabled:', gc_enabled, 'garbage:', garbage)
    for obj in garbage:
        print('  object:', obj)
        for ref in gc.get_referrers(obj):
            print('    referrer:', ref
