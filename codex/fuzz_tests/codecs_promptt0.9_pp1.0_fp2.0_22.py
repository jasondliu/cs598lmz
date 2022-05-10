import codecs
# Test codecs.register_error / getstate / setstate
import os
import pickle
from test import test_support
import unittest


class misc_tests(unittest.TestCase):
    def test_register_error(self):
        for name in dir(codecs):
            if name.endswith("_error"):
                err = getattr(codecs, name)
                new_name = "new-" + name
                codecs.register_error(new_name, err)

    def test_getstate_setstate(self):
        stream1 = codecs.getreader("utf-8")("xyz")
        stream2 = codecs.getreader("utf-8")("zyx")
        stream2.read(2)
        state = stream2.__getstate__()

        stream1.__setstate__(state)
        stream1.read(1)
        self.assertEqual(stream1.read(1), "x")
        self.assertEqual(stream2.read(1), "")

    def test_stream_io_wrapping(self):
