import weakref
# Test weakref.ref() to see if it works properly
def testRef():
    import weakref
    class Dummy(object):
        pass
    d = Dummy()
    d.attr = Dummy()
    
    r = weakref.ref(d.attr)
    print r()
    assert r() is d.attr
    del d.attr
    assert r() is None
    d.attr = Dummy()
    assert r() is None
    print "testRef() passed!"
testRef()

# Test tp_weakreflist to see if it works properly
def testWeakRefList():
    # Create Python classes that have a tp_weaklist slot
    Object = type.__new__(type, "Object", (), {})
    Object.__name__ = 'Object'
    Object.__doc__ = None
    new_slots = ['attr', '__class__', '__dict__']
    new_slots.append('__weakreflist__')
    Object.__slots__ = new_slots
    
    class Node(Object):
        pass
   
