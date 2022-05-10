import weakref
# Test weakref.ref() to see if it works properly
def testRef():
    import weakref
    class Dummy(object):
        pass
    d = Dummy()
    d.attr = Dummy()
    
    r = weakref.ref(d.attr)
