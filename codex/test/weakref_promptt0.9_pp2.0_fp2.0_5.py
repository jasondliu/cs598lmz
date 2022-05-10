import weakref
# Test weakref.ref(func), weakref.prooxy(obj), and weakref.finalize.
import unittest
import re
import gc
import sys

# Base Test for testing the WeakKeyDictionary and WeakValueDictionary.
# Derived classes must define the attribute dict which is a WeakKeyDictionary
# or WeakValueDictionary to be tested.  self.proxy is the object being
# proxied.
class TestWeakDictionary:

    rawdict = None

    def setUp(self):
        self.dict = self.type2test()
        self.proxy = self.dict.proxied
        self.foo = Foo(self.dict)
        if self.type2test.__name__ == "WeakValueDictionary":
            self.foo2 = Foo(self.dict)
            self.foo2.name = "foo2"

    def teardown(self):
        self.dict = None
        self.proxy = None
        self.foo = None
        self.rawdict = None

