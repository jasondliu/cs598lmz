fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fp = fn.__code__.co_firstlineno

ga = (a for a in ())
fn.__code__ = ga
fa = fn.__code__.co_firstlineno


class A(object):
    def foo(self):
        raise Exception("bar")


class B(A):
    pass


class C(object):

    def __eq__(self, *args):
        return bool()


class D(object):

    def __eq__(self, *args):
        return False


class E(object):

    def __eq__(self, *args):
        return 23
