import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect, gc.get_referrers and gc.garbage (see issue #10405)

def ref():
    return weakref.ref(gc.garbage[0])

def check(ref):
    gc.collect()
    if ref() is not None:
        print("Error: gc.garbage[0] not collected")
        raise SystemExit

def test():
    gc.collect()
    gc.garbage.append(C())
    r = ref()
    check(r)
    gc.garbage.append(C())
    check(r)
    v = gc.garbage.pop()
    check(r)
    del v
    check(r)
    gc.garbage.append(C())
    check(r)
    gc.garbage.append(C())
    check(r)
    del gc.garbage[:]
    check(r)
    print("Success")

test()
