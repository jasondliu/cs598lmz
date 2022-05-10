import gc, weakref
import unittest
import sys

class A: pass

def create_cycle(a):
    a.x = a

def create_big_cycle(n):
    a = A()
    for i in range(n):
        a.i = A()
        a = a.i
    return a

class TestWeakref(unittest.TestCase):

    def test_basic(self):
        a = A()
        a.foo = 42
        ar = weakref.ref(a)
        self.assertEqual(ar().__class__, A)
        self.assertEqual(ar().foo, 42)
        del a
        self.assert_(ar() is None)
        self.assert_(not hasattr(A, '__del__'))

    def test_basic_callback(self):
        l = []
        def callback(obj):
            l.append(obj)
        a = A()
        a.foo = 42
        ar = weakref.ref(a, callback)
