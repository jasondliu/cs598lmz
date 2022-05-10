import gc, weakref
import sys
import time
import traceback
import unittest
from weakref import ref as WeakKeyDictionary


class TestBase(unittest.TestCase):
    def setUp(self):
        gc.collect()
        self.callbacks = []

    def tearDown(self):
        gc.collect()
        for ref in self.callbacks:
            self.assertIsNone(ref(),
                "callback %s:%s still live!" % (ref(), id(ref())))

    def callback(self, ref):
        self.assertIsInstance(ref, weakref.ReferenceType)
        self.callbacks.append(ref)
        self.assertIs(ref(), self.obj)


class BasicTest(TestBase):
    obj = "hello world"

    def test_basic(self):
        self.assertIs(self.obj, "hello world")
        p = WeakKeyDictionary(self.obj, self.callback)
        self.assertIs(p(), self.obj)
        del self.obj
        gc.collect()
