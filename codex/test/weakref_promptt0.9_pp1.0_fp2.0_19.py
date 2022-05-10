import weakref
# Test weakref.ref to a tuple of class instances.  This used to segfault
# because the class instances were not getting their tp_clear hooked.

# The following line would cause an exception
#class Foo:
#    pass

class WeakRefClearedException(Exception):
    pass

def ClearWeakRef(ref, arg):
    try:
        x = ref()
    except:
        raise WeakRefClearedException

def Test():
    op('obj id', id)
    op('tuple id', id(tuple))
    x1 = tuple([2, 3, 4])
    x2 = (10, 20)
    x = (Foo(), x1, x2)
    r = weakref.ref(x, ClearWeakRef)
    version = sys.version
    try:
        sys.version
    except:
        print('modulo sys.version')
    else:
        print('no excpetion')

    print('weakref tester ok')
Test()
