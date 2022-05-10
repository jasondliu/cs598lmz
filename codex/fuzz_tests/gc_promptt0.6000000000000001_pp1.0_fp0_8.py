import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# Test gc.collect()

def run_collect():
    gc.collect()
    if verbose:
        print("%d collectable" % len(gc.garbage))
        for x in gc.garbage:
            print("  ", x)

class A:
    def __init__(self):
        self.b = B(self)
        self.c = C(self)
        self.d = D(self)
    def __repr__(self):
        return "<A>"
    def __del__(self):
        if verbose:
            print("A.__del__")

class B:
    def __init__(self, a):
        self.a = a
    def __repr__(self):
        return "<B>"
    def __del__(self):
        if verbose:
            print("B.__del__")

class C:
    def __init__(self, a):
        self.a = a
    def __repr__(self):
        return "<C>"
   
