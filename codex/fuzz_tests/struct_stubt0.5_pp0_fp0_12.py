from _struct import Struct
s = Struct.__new__(Struct)
s.size = lambda: 0

class C(object):
    def __init__(self):
        pass

    def meth(self):
        pass

def f():
    pass

def g():
    pass

class D(C):
    def __init__(self):
        C.__init__(self)
        self.x = 1
        self.y = 2
        self.z = 3
        self.w = 4
        self.v = 5
        self.u = 6
        self.t = 7
        self.s = 8
        self.r = 9
        self.q = 10
        self.p = 11
        self.o = 12
        self.n = 13
        self.m = 14
        self.l = 15
        self.k = 16
        self.j = 17
        self.i = 18
        self.h = 19
        self.g = 20
        self.f = 21
        self.e = 22
        self.d = 23
        self.c = 24
        self.b = 25

