import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self):
        self.data = [1, 2, 3]

class Bar:
    def __init__(self):
        self.data = Foo()

def test():
    b = Bar()
    f = b.data
    b.data = None
    del b
    gc.collect()
    return f

f = test()
print(f.data)

# Test gc.get_referrers()

def test():
    b = Bar()
    f = b.data
    b.data = None
    del b
    return f

f = test()
print(gc.get_referrers(f))

# Test gc.get_referents()

def test():
    b = Bar()
    f = b.data
    b.data = None
    del b
    return f

f = test()
print(gc.get_referents(f))

# Test gc.get_objects()

def test():
    b = Bar()
