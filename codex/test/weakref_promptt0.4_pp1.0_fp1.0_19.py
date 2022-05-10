import weakref
# Test weakref.ref(x).__call__()

class Foo:
    pass

def bar(x):
    return x

def test_call():
    o = Foo()
    ref = weakref.ref(o)
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
    assert ref() is o
   
