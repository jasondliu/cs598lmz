import gc, weakref
import pdb

def _r_del(ref):
    print '_r_del'
    print ref
    print ref()

class Foo(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
        self.c = 'c'
        self.d = 'd'
        self.e = 'e'
        self.f = 'f'
        self.g = 'g'
        self.h = 'h'
        self.i = 'i'
        self.j = 'j'
        self.k = 'k'
        self.l = 'l'
        self.m = 'm'
        self.n = 'n'
        self.o = 'o'
        self.p = 'p'
        self.q = 'q'
        self.r = 'r'
        self.s = 's'
        self.t = 't'
        self.u = 'u'
        self.v = 'v'
        self.w = 'w'
