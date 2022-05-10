import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def bar():
    return Foo()

def main():
    f = bar()
    wr = weakref.ref(f)
    f = None
    gc.collect()
    assert wr() is None

main()
print('passed')
