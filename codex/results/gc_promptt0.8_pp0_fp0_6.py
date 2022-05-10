import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when weakref callback is hanging
class HangingRef(weakref.ref):
    def __call__(self):
        while True:
            pass

def test_hanging_ref():
    p = Process(target=_test_hanging_ref)
    try:
        p.start()
        p.join(timeout=0.2)
        if p.is_alive():
            p.terminate()
    finally:
        p.join()

def _test_hanging_ref():
    s = S()
    h = HangingRef(s)
    # id(s) is added to a set in the callback, this is
    # how we detect that the callback has been called
    assert id(s) not in collect_ids
    del s
    gc.collect()
    assert id(h()) == 0 or id(h()) not in collect_ids, `collect_ids`
    assert id(h()) == 0

if __name__ == "__main__":
    test_hanging_ref()
