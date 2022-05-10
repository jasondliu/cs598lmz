import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
done = ''
class Test:
    def __init__(self, name):
        global done
        # all test instances are added to this list, but are not known
        # to the garbage collector
        all.append(self)
        self.name = name
    def __del__(self):
        global done
        # indirect through the global all: at this point the
        # decref of all has been done, and the garbage collector will
        # free the list if all elements are removed from it (which
        # will call __del__ again, but never mind)
        c = len(all)
        for i in range(c):
            test = all[0]
            test.__class__.test(test)
            del all[0]
        done = 'done'
    def test(self):
        if verbose:
            print self.name

def test_trivial():
    test = Test('test_trivial')
    # add a reference, and delete it immediately again
    ref = weakref.ref(Test('trivial'))
    del
