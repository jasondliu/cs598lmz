import weakref
# Test weakref.ref() and weakref.proxy()

import weakref
import unittest
import gc
import sys
import pickle

class C:
    pass

def callback(r):
    callback.called = True
    callback.ref = r

class D:
    pass

class E(object):
    pass

class F(object):
    def __init__(self, x):
        self.x = x

class G(object):
    def __init__(self, x):
        self.x = x

    def __hash__(self):
        return hash(self.x)

    def __eq__(self, other):
        return self.x == other.x

class H(object):
    def __init__(self, x):
        self.x = x

    def __hash__(self):
        return hash(self.x)

    def __eq__(self, other):
        return self.x == other.x

    def __call__(self):
        pass

class I(object):
    def __init__(self
