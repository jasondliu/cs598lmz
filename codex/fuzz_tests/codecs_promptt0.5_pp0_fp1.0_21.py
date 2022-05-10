import codecs
# Test codecs.register_error
#
# This is based on test_codecs.py by Marc-Andre Lemburg, but with the
# error handler replaced by a custom one.

import unittest
import test.support
import test.test_support

# Error handler

class CodecRegError(Exception):
    pass

class CodecRegErrorHandler:

    def __init__(self, errors='strict'):
        self.errors = errors

    def __call__(self, exception):
        if self.errors == 'strict':
            raise exception
        elif self.errors == 'ignore':
            return (u'', exception.end)
        elif self.errors == 'replace':
            return (u'', exception.end)
        else:
            raise CodecRegError(
                  'unexpected error handling setting: %r' % self.errors)

# Encoder

class CodecRegTestEncoder(codecs.Codec):

    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors,
                                     {
