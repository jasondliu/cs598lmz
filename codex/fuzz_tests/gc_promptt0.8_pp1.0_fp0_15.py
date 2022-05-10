import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect_generations()

def gc_collect(gen=2):
    # Try to collect everything that is collectable.  gen indicates
    # which generations to collect.
    for i in range(gen):
        n = gc.collect(i)
        if n > 0:
            print "collecting gen", i, "unreachable objects:", n
        else:
            break
    return "done"

class C(object):
    def __init__(self, y):
        self.y = y
        self.next = self

    def __del__(self):
        pass

def f():
    # Put some stuff on the heap
    x = C(1)
    u = x.next
    v = x.next
    x.next = None
    try:
        x.next = u
    except ValueError:
        print "ValueError"
    v.next = u
    try:
        x.next = u
    except ValueError:
        print "ValueError"
    # There are now four objects:
    # x, u,
