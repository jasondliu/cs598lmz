fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code


class I:
    def __init__(self):
        self.called = False

    def __del__(self):
        self.called = True


class A:
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

    def __getattr__(self, x):
        if x == 'k':
            return x
        else:
            raise AttributeError


import sys

class B:
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
        self.k =
