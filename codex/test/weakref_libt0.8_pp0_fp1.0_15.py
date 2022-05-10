import weakref

from contextlib import contextmanager

from . import combinators
from . import regexp
from . import utils


class Parser(object):

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)

    def parse(self, state):
        return self.f(state)

    def __eq__(self, other):
        return isinstance(other, Parser) and self.f == other.f

    def __and__(self, other):
        return combinators.And(self, other)

    def __rand__(self, other):
        return combinators.And(other, self)

    def __invert__(self):
        return combinators.Not(self)

    def __or__(self, other):
        return combinators.Or(self, other)

    def __ror__(self, other):
        return combinators.Or(other, self)

