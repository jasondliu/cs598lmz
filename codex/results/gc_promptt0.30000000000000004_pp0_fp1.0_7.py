import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    def __init__(self, name):
        self.name = name
        self.b = B(self)
    def __del__(self):
        print "del", self.name

class B:
    def __init__(self, a):
        self.a = a
    def __del__(self):
        print "del B of", self.a.name

a = A("a")
b = B(a)
a.b = b
del a
del b
gc.collect()

# Test gc.garbage
class C:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print "del", self.name

c1 = C("c1")
c2 = C("c2")
c3 = C("c3")
c4 = C("c4")
c5 = C("c5")
c6 = C("c6")

c1.next = c2
c2.next = c3
c3.next =
