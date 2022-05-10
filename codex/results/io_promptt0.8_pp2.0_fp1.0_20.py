import io
# Test io.RawIOBase

from test import support
import unittest


class ReadTestMixin:

    def _test_read(self, testcase, method):
        self.assertEqual(method(0), b'')
        self.assertRaises(ValueError, method, -1)
        self.assertRaises(TypeError, method, None)
        self.assertRaises(TypeError, method, 'x')
        self.assertRaises(TypeError, method, 0.5)
        self.assertRaises(TypeError, method, 0xFFFF)
        self.assertRaises(TypeError, method, 0xFFFFFFFFFFFFFFFF)


class ReadintoTestMixin:

    def _test_readinto(self, testcase, method):
        self.assertRaises(TypeError, method, None)


class UniversalNewlineTestMixin:

    def test_universal(self):
        with self.assertRaises(io.UnsupportedOperation):
            self.FileIO.newlines


class AppendTestMixin:

    def _test_append(self, testcase,
