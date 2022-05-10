import weakref
# Test weakref.ref(obj)

def dying(wr):
    print ("dying", wr)

def dead(wr):
    print ("dead", wr)

def test1():
    class MyObject: pass
    obj = MyObject()
    ref = weakref.ref(obj)
    assert (ref() is obj)
    obj = None
    assert ref() is None

# Test weakref.ref(obj, callback(ref))
def test2():
    class MyObject: pass
    obj = MyObject()
    ref = weakref.ref(obj, dying)
    assert (ref() is obj)
    obj = None
    assert ref() is None

# Test weakref.ref(obj, callback(ref), callback(ref))
def test3():
    class MyObject: pass
    obj = MyObject()
    ref = weakref.ref(obj, dying, dead)
    assert (ref() is obj)
    obj = None
    assert ref() is None

# Test weakref.ref(obj, None)
def test4():
    import sys
