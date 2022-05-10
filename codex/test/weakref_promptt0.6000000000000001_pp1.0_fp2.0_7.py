import weakref
# Test weakref.ref() for callable objects.
import sys
import gc
import operator
import functools


class A(object):

    def __init__(self, x):
        self.x = x

    def __call__(self):
        return self.x


def callback(r):
    r().callback()


class B(object):

    def __init__(self, x):
        self.x = x

    def callback(self):
        pass


class C(A):

    def __init__(self, x):
        A.__init__(self, x)

    def __call__(self, *args):
        return self.x


class D(C):

    def __init__(self, x):
        C.__init__(self, x)

    def __call__(self, *args, **kwargs):
        return self.x


# This class is used to test whether the callback is called
# with the correct reference object (and not just a true value)
