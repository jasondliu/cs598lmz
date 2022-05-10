import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Test:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4
        self.e = 5
        self.f = 6
        self.g = 7
        self.h = 8
        self.i = 9
        self.j = 10
        self.k = 11
        self.l = 12
        self.m = 13
        self.n = 14
        self.o = 15
        self.p = 16
        self.q = 17
        self.r = 18
        self.s = 19
        self.t = 20
        self.u = 21
        self.v = 22
        self.w = 23
        self.x = 24
        self.y = 25
        self.z = 26

def test():
    t1 = Test()
    t2 = Test()
    t3 = Test()
    t4 = Test()
    t5 = Test()
    t6 = Test()
    t7 = Test()
    t8
