import weakref
# Test weakref.ref(x)
def f():
    x = weakref.ref(42)
    assert x() == 42
    del x
    try:
        x()
    except ReferenceError:
        pass
    else:
        raise Exception
f()

# Test weakref.ref(x, callback)
def f():
    x = weakref.ref(42, lambda x: None)
    assert x() == 42
    del x
    try:
        x()
    except ReferenceError:
        pass
    else:
        raise Exception
f()

# Test weakref.proxy(x)
def f():
    x = weakref.proxy(42)
    assert x == 42
    del x
    try:
        x
    except ReferenceError:
        pass
    else:
        raise Exception
f()

# Test weakref.getweakrefcount(x)
def f():
    x = 42
    assert weakref.getweakrefcount(x) == 0
f()

# Test weakref.getweakrefs(x)
