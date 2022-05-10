import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Foo %r %r>" % (self.x, self.y)

    def __del__(self):
        print "__del__"

def f():
    print "enter f"
    a = Foo(1, 2)
    print "exit f"

def g():
    print "enter g"
    a = Foo(1, 2)
    a.x = Foo(3, 4)
    print "exit g"

def h():
    print "enter h"
    a = Foo(1, 2)
    a.x = Foo(3, 4)
    a.y = a
    print "exit h"

def i():
    print "enter i"
    a = Foo(1, 2)
    a.x = Foo(3, 4)
    a.y = a
    del a
    print "exit i"

def j
