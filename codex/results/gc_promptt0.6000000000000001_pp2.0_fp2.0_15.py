import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# In this example, gc.collect() is called to ensure that the
# weakref callback is called.

class MyClass:
    pass

def callback(wr):
    print 'Callback:', wr

def callback_with_param(wr, param):
    print 'Callback with parameter:', wr, param

def doit():
    obj = MyClass()
    print 'obj:', obj
    print 'obj refcount:', sys.getrefcount(obj)

    wr = weakref.ref(obj, callback)
    print 'wr:', wr
    print 'wr refcount:', sys.getrefcount(wr)

    wrp = weakref.ref(obj, callback_with_param, 'extra argument')
    print 'wrp:', wrp
    print 'wrp refcount:', sys.getrefcount(wrp)

    wr = None
    wrp = None
    obj = None

    gc.collect()

def main():
    for i in range(3):
        doit()

if __name__ == '__
