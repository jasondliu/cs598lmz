import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs.
# A weakref to a list is created after the list has been created
# and the list is assigned to wr().  All references to the list
# are then deleted.  The weakref is then accessed, at which point
# it should have been finalized.  Finally, wr() is set to None
# and gc.collect() is called.

class A:
    pass

def soft_callback(wr, A):
    print 'soft_callback: weakref dead'

def strong_callback(wr, A):
    print 'strong_callback: weakref dead'

def check_callback(wr, A):
    print 'check_callback: weakref dead'

class MyList(list):
    def __del__(self):
        print 'MyList.__del__'

wr = None
def test():
    global wr
    a = A()
    l = MyList([a])

    wr = weakref.ref(l, callback)
    print wr()
    print wr() is l
    print wr() is None
    del l
    g
