fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_slicing
def f():
    pass

f.__code__ = (1, 2, 3, 4)
f()

# test_setslice
def f():
    pass

f.__code__ = (1, 2, 3, 4)
f()

# test_delitem
def f():
    pass

f.__code__ = (1, 2, 3, 4)
f()

# test_delslice
def f():
    pass

f.__code__ = (1, 2, 3, 4)
f()

# test_setitem_bad_index
def f():
    pass

f.__code__ = (1, 2, 3, 4)
f()

# test_setslice_bad_index
def f():
    pass

f.__code__ = (1, 2, 3, 4)
f()

# test_delitem_bad_index
def f():
    pass

f.__code__ = (1, 2, 3,
