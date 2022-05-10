import weakref
# Test weakref.ref() function


class C:

    def __init__(self):
        self.a = 1
    if 0:
        b = 2

def kill(x):
    print(x())


c = C()
cr = weakref.ref(c, kill)
print(cr())
del c

# Test __init__ and __new__
import sys
from weakref import WeakSet


class MyMeta(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance


class A(metaclass=MyMeta):
    instances = WeakSet()
    apa = 42

    def __init__(self, *args, **kwargs):
        self.instances.add(self)
        self.args = args
        self.kwargs = kwargs
        self.called__init__ = True

    def __new__(cls, *args, **kwargs):

