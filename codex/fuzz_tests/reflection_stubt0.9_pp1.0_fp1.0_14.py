fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
gi.gi_code = 1
fn()


def f():
    i == 1
    i = 2
    i


eval(f.__code__)


class A:

    def f(self):
        x not in y
        self.x == 1
        while 1:
            pass


class A:

    def f(self):
        if x == 1:
            pass


class A(object):

    def f(self):
        if x == 1:
            pass


class A:

    def __init__(self):
        if x == 1:
            pass

print(A.f.__code__.co_varnames[:
      A.f.__code__.co_argcount])
assert A.f.__code__.co_varnames[:A.
       f.__code__.co_argcount] == ('self',)
print(getattr(A.__init__, '__code__').co_varnames[1:
      getattr(A.__init__, '__code__
