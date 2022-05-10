import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, x):
        self.x = x
    def __del__(self):
        print "deleting", self.x

f = Foo(1)
f = Foo(2)
f = Foo(3)
f = Foo(4)
f = Foo(5)
f = Foo(6)
f = Foo(7)
f = Foo(8)
f = Foo(9)
f = Foo(10)
f = Foo(11)
f = Foo(12)
f = Foo(13)
f = Foo(14)
f = Foo(15)
f = Foo(16)
f = Foo(17)
f = Foo(18)
f = Foo(19)
f = Foo(20)
f = Foo(21)
f = Foo(22)
f = Foo(23)
f = Foo(24)
f = Foo(25)
f = Foo(26)
f = Foo(27)
f = Foo(28)
f = Foo(29)
f = Foo(30)
