import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    def __init__(self):
        self.refs = [None] * 2

    def __repr__(self):
        return "<Foo at %x>" % id(self)

def create_graph():
    a = Foo()
    b = Foo()
    a.refs[0] = b
    b.refs[1] = a
    return a

gc.collect()

def test1():
    l = []
    for i in range(100):
        l.append(create_graph())
        if i % 10 == 0:
            gc.collect()
            assert not gc.garbage

def test2():
    l = []
    for i in range(100):
        l.append(create_graph())
        if i % 10 == 0:
            del l[:]
            assert gc.garbage
            gc.collect()
            assert not gc.garbage

def test3():
    class A(object):
        pass
    class B(A):
        pass
