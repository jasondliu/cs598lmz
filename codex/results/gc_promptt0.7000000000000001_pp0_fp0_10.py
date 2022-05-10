import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on a weakref to a cycle
def test():
    class A:
        def __init__(self, x):
            self.x = x
        def __del__(self):
            print ("collecting", self.x)
    a1 = A(1)
    a2 = A(2)
    weak_a1 = weakref.ref(a1)
    weak_a2 = weakref.ref(a2)
    a1.x = a2
    a2.x = a1
    del a1, a2
    print (weak_a1(), weak_a2())
    gc.collect()
    print (weak_a1(), weak_a2())
    return weak_a1, weak_a2

# Test gc.collect() on a weakref to a cycle that has been broken
def test2():
    class A:
        def __init__(self, x):
            self.x = x
        def __del__(self):
            print ("collecting", self.x)
    a1 = A(1)
   
