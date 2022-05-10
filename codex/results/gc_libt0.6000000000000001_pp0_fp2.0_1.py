import gc, weakref, copy

from unittest import TestCase
from test.test_support import (
    run_unittest, captured_stdout, captured_stderr,
    check_warnings, check_no_resource_warning,
)

class TestException(Exception):
    pass

class TestWeakref(TestCase):

    def callback(self, object_ref):
        self.called = True

    def test_basic(self):
        object = object()
        object_id = id(object)
        object_ref = weakref.ref(object, self.callback)
        object_ref_id = id(object_ref)
        del object
        gc.collect()
        self.assertEqual(self.called, True)
        self.called = False
        object = object_ref()
        object_id2 = id(object)
        self.assertEqual(object_id, object_id2)
        del object
        self.assertEqual(self.called, False)
        self.assertEqual(object_ref(), None)
        self.
