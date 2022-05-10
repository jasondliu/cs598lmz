import weakref
# Test weakref.ref:
#
#   o Refs to temporary objects are illegal (including to the temporary
#     that is the target of the __init__ call).

def test(C):
    # Test weakref.ref(C(...)) raises error
    try:
        weakref.ref(C(0))
    except TypeError, e:
        print 'weakref.ref(%r(0)) raises TypeError: %s' % (C, e)
        # assert e.args == ('cannot create weak reference to temporary',),e
    except RuntimeError, e:
        print 'weakref.ref(%r(0)) raises RuntimeError: %s' % (C, e)
    else:
        print 'weakref.ref(%r(0)) does not raise TypeError' % C
    if hasattr(C, '__del__'):
        # Test del C(...), weakref.ref(x) raises error
        x = C(1)
        del C
        try:
            weakref.ref(x)
        except TypeError, e:
            print 'weak
