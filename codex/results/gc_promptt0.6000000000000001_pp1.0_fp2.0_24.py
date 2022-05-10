import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __del__(self):
        print "deleted"

class Bar:
    def foo(self):
        return Foo()

def main():
    b = Bar()
    b.foo()
    print "gc.collect():", gc.collect()
    print "gc.collect():", gc.collect()

main()

# Test gc.get_referrers()

class Foo:
    def __init__(self, n):
        self.n = n
    def __repr__(self):
        return "<Foo %d>" % self.n

def make_foo(n):
    return Foo(n)

def main():
    f1 = make_foo(1)
    f2 = make_foo(2)
    f3 = make_foo(3)
    f4 = make_foo(4)
    f5 = make_foo(5)
    l = [f1, f2, f3, f4, f5]
    print l
    print gc.get_
