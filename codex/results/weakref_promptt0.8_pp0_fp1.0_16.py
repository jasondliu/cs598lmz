import weakref
# Test weakref.ref in unittest/test_weakref.py.

from test import mapping_tests
from test import string_tests
from UserDict import DictMixin

from test.test_support import run_unittest, TestFailed, check_impl_detail

from _weakref import getweakrefcount, getweakrefs
from _weakrefset import WeakSet, _IterationGuard


class GeneralMappingTests(mapping_tests.BasicTestMappingProtocol):
    type2test = WeakKeyDictionary

    def test_init(self):
        # calling built-in types without argument must return empty
        self.assertEqual(WeakKeyDictionary(), {})
        self.assertIsNot(WeakKeyDictionary(), WeakKeyDictionary())
        self.assertEqual(WeakValueDictionary(), {})
        self.assertIsNot(WeakValueDictionary(), WeakValueDictionary())

    def test_repr(self):
        d = WeakKeyDictionary(value=1)
        self.assertEqual(repr(d), 'WeakKeyDictionary({})')

