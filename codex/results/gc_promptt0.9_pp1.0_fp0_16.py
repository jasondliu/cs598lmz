import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
def f():
    with weakref.ref(obj) as w:
        assert gc.collect() > 0
        assert w() is None

obj = [10]
f()
del obj
print 'ok'
gc.collect()

# test weakref.proxy, again
def f():
    with weakref.proxy(obj) as p:
        assert gc.collect() > 0
        try:
            p.foo
        except ReferenceError:
            pass
        else:
            print 'failed 1'

obj = [10]
f()
del obj
print 'ok'
gc.collect()

# test weakref.proxy to frame
def f():
    with weakref.proxy(obj) as p:
        assert gc.collect() > 0
        try:
            p.foo
        except ReferenceError:
            pass
        else:
            print 'failed 1'

obj = sys._getframe()
f()
del obj
print 'ok'
gc.collect()
