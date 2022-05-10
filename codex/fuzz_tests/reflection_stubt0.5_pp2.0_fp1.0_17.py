fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__module__ = 'mod'
fn.__dict__ = dict(a=1)
fn.__defaults__ = (2, 3)
fn.__closure__ = (4,)
fn.__annotations__ = dict(b=5)
fn.__kwdefaults__ = dict(c=6)


def f():
    return 1


class C:
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


class D(C):
    def __init__(self):
        super().__init__()
        self.k = 11
        self.l = 12
        self.m = 13
        self.n = 14
        self.o = 15
       
