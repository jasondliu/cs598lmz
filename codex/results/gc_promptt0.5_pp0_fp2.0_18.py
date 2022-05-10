import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

def create_cycle(n):
    l = []
    for i in range(n):
        l.append(l)
    del l

class A:
    def __del__(self):
        print("deleting", self)

def create_cycle2(n):
    l = []
    for i in range(n):
        l.append(A())
    del l

def create_cycle3(n):
    l = []
    for i in range(n):
        l.append(weakref.ref(l))
    del l

def create_cycle4(n):
    l = []
    for i in range(n):
        l.append(l)
    gc.collect()
    del l

def create_cycle5(n):
    l = []
    for i in range(n):
        l.append(l)
    gc.collect()
    l.append(l)
    del l

def create_cycle6(n):
    l = []
    for i in range(n):
