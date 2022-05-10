import gc, weakref

def test():
    class A:
        pass
    a = A()
    b = A()
    a.b = b
    b.a = a
    del a
    del b
    gc.collect()
    assert len(gc.garbage) == 0

test()

class A:
    pass

a = A()
b = A()
a.b = b
b.a = a
del a
del b
gc.collect()
