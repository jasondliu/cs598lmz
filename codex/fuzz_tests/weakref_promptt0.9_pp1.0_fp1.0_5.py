import weakref
# Test weakref.ref for callable objects.
# (Generic weakref tests are in test_weakref.py)


class Callable(object):

    def __call__(self, *args):
        return args


class Dummy(object):
    pass


class Base(object):

    def __call__(self, *args):
        return args


class Derived(Base):
    pass


class Mitigated(object):

    def __new__(cls):
        return Base()


class Noop(object):

    def __call__(self, *args):
        return self


class Broken(object):

    def __call__(self, *args):
        raise SystemError


class Exc(object):

    def __call__(self, *args):
        raise ValueError


class Slots(object):
    __slots__ = ['a']

    def __call__(self, *args):
        return args


class Overload:

    def __call__(self, x):
        return 'plain', x

    def __call__(self, x, y
