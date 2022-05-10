import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with an explicit callback
def test_callback(arg):
    #callback.append(ref)
    callback_func.append(arg())
ref = []
callback = []
callback_func = []
for i in range(25):
    gc.collect(i, callback)
print len(callback)
print len(callback_func)
for item in callback_func:
    print item
print '\n'
gc.set_debug(0)


def test_finalize():
    class FinalizeClass(object):
        def __init__(self):
            self.alive = True
        def __del__(self):
            print "FinalizeClass.__del__"
            self.alive = False
    obj = FinalizeClass()
    r = weakref.ref(obj, lambda r: print "Dead!")
    del obj
    print r()
test_finalize()


# one class - mulitple finalize
class Orderable:
    _instances = set()
    _id = 0

    @classmethod
    def __order(cls, x
