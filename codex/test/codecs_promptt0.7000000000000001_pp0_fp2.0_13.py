import codecs
# Test codecs.register_error for a user-defined error handler.
import json
import unittest


class MyError(Exception):
    pass


def my_error_handler(error):
    return (u'', error.start + 1)


class TestRegistration(unittest.TestCase):
    def test_register(self):
        self.assertTrue(codecs.lookup_error('strict') is not my_error_handler)
        codecs.register_error('strict', my_error_handler)
        self.assertTrue(codecs.lookup_error('strict') is my_error_handler)

    def test_unregister(self):
        self.assertTrue(codecs.lookup_error('strict') is not my_error_handler)
        codecs.register_error('strict', my_error_handler)
        self.assertTrue(codecs.lookup_error('strict') is my_error_handler)
        codecs.register_error('strict', None)
