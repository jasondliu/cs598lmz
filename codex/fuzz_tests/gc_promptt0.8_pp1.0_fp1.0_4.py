import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on a frozen object (not collectable).
class X(object):
    pass
x = X()
x.a = weakref.ref(x)
x.b = weakref.ref(x)
del x
gc.collect()

#
# Test gc.collect() on a cyclic trash object with a custom destructor.
#

class Foo(object):
    def __init__(self, name):
        self.name = name
        self.nested = None

    def __repr__(self):
        return "<Foo %s>" % (self.name,)

    def __del__(self):
        print "Destructor called for", self, self.nested
        if self.nested:
            print "The following exception is expected"
            raise ValueError("crash")

def make_cyclic_trash():
    foo = Foo("top")
    foo.nested = Foo("nested")
    foo.nested.nested = foo
    return foo

print "\nCrash test.  The following exception is expected:"
foo =
