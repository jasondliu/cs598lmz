import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() not mistakenly collecting callback
# test for issue #13975

class Test:

    def __init__(self):
        self.callback = weakref.ref(self.handler)
        self.done = False

    def handler(self, ref):
        self.done = True


def f():
    t = Test()
    weakref.ref(t, t.callback)
    t = None
    gc.collect()
    if not ref.done:
        raise RuntimeError("Did not trigger callback")

threading.Thread(target=f).start()
