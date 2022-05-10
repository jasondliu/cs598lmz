import weakref
# Test weakref.ref()
def f():
    x = 42
    y = weakref.ref(x)
    assert y() == 42
    print(y())
    # del x
    # assert y() is None
    # assert y() is None

