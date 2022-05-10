import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect(2)
# Test gc.collect()
# Test del
# Test weakref.proxy

class Baz(object):
    def __del__(self):
        try:
            print "Baz.__del__"
        except:
            print "Baz.__del__ raises an exception"

class Foo(object):
    def __del__(self):
        print "Foo.__del__"

def callback(o):
    print "callback"

def main():
    gc.set_debug(gc.DEBUG_LEAK)
    # Test gc.collect(2)
    baz = Baz()
    wr = weakref.ref(baz, callback)
    del baz
    print gc.collect(2)
    print "end of test 1"
    del wr
    print gc.collect(2)
    print "end of test 2"
    # Test gc.collect()
    baz = Baz()
    wr = weakref.ref(baz, callback)
    del baz
    print gc.collect()

