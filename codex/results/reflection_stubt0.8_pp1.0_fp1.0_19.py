fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(lambda: 0).__code__
type(fn.__code__).__hash__ = lambda x: hash(None)
fn()

s = "Ejike"
s = s.encode("utf-8")
s = s.decode("utf-8")
s = eval("s.capitalize()")

import sys

class A:
    def __init__(self):
        self.__class__.b = 1

A()

class C:
    def __del__(self):
        raise Exception

class B(C):
    def __new__(cls):
        return 1

B()


class A:
    def __del__(self):
        pass

    def __delattr__(self, name):
        raise Exception


del A()


class A:
    def __del__(self):
        pass

    def __delattr__(self, name):
        pass

class B(A):
    def __del__(self):
        raise Exception

    def __delattr
