import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

class Bar(object):
    pass

def main():
    # Create a reference cycle
    f = Foo()
    b = Bar()
    f.x = b
    b.y = f

    # Create a reference cycle
    f = Foo()
    b = Bar()
    f.x = b
    b.y = f

    # Create a reference cycle
    f = Foo()
    b = Bar()
    f.x = b
    b.y = f

    # Create a reference cycle
    f = Foo()
    b = Bar()
    f.x = b
    b.y = f

    # Create a reference cycle
    f = Foo()
    b = Bar()
    f.x = b
    b.y = f

    # Create a reference cycle
    f = Foo()
    b = Bar()
    f.x = b
    b.y = f

    # Create a reference cycle
    f = Foo()
    b = Bar()
    f.x = b
    b.y
