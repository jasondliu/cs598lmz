import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback
class C:
    pass

def callback(w):
    print 'callback'

def main():
    c = C()
    r = weakref.ref(c, callback)
    print 'collecting'
    gc.collect()
    print 'done'
    del c
    print 'collecting'
    gc.collect()
    print 'done'

main()
# Test gc.collect() with an uncollectable object with a finalizer
class C:
    def __del__(self):
        print 'del'

def main():
    c = C()
    gc.collect()
    print 'collecting'
    gc.collect()
    print 'done'
    del c
    print 'collecting'
    gc.collect()
    print 'done'

main()
# Test gc.collect() with an uncollectable object with a finalizer that
# is weakly referred to
class C:
    def __del__(self):
        print 'del'

def main():
    c =
