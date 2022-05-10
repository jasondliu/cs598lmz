import codecs
# Test codecs.register_error
import io
import os
import sys
import unittest
import warnings
from test import support
from test.support import bigmemtest, bigaddrspacetest, _2G, _4G


class TestBase:
    # Utility functions for testing codecs

    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, self.encoding)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, self.encoding)

    def assertEqual(self, first, second, msg=None):
        if first != second:
            raise self.failureException(msg or '%r != %r' % (first, second))

    def assertRaises(self, exc, fun, *args, **kwds):
        try:
            fun(*args, **kwds)
        except exc:
            pass
        else:
            raise self.failureException("%s not raised" % exc.__name__)

    def assertTrue(
