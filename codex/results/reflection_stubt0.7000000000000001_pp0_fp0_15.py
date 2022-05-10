fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__module__ = gi.gi_module
fn()


def fn():
    return fn.__code__.co_firstlineno


assert fn() == fn.__code__.co_firstlineno == fn.__code__.co_lnotab[0]


class C:
    def __init__(self, what):
        self.what = what

    def method(self):
        return self.what


def f(x):
    return x


class D:
    def __init__(self, what):
        self.what = what

    def method(self):
        return self.what


def g(x):
    return x


class E:
    def __init__(self, what):
        self.what = what

    def method(self):
        return self.what


def h(x):
    return x


class F:
    def __init__(self, what):
        self.what = what

    def method(self):
        return self.what


def i(
