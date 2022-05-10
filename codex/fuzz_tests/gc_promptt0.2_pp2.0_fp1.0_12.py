import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def bar():
    print "in bar"
    foo = Foo()
    foo.func = bar
    foo.wr = weakref.ref(foo)
    return foo

def main():
    print "in main"
    foo = bar()
    foo = None
    gc.collect()
    print "end of main"

main()

# Test gc.get_referrers()

class Foo(object):
    pass

def bar():
    print "in bar"
    foo = Foo()
    foo.func = bar
    foo.wr = weakref.ref(foo)
    return foo

def main():
    print "in main"
    foo = bar()
    foo = None
    gc.collect()
    print "end of main"

main()

# Test gc.get_referents()

class Foo(object):
    pass

def bar():
    print "in bar"
    foo = Foo()
    foo.func = bar
    foo.wr
