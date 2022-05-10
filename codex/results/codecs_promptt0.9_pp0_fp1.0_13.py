import codecs
# Test codecs.register_error()
import unittest
from test import test_support
import warnings

def search_function(encoding):
    if 'bad' in encoding:
        class Codec(codecs.Codec):
            def encode(self, input, errors='strict'):
                return codecs.charmap_encode(input, errors,
                    {'b': u'/', 'a': u'+'}, 'ignore')
            def decode(self, input, errors='strict'):
                return codecs.charmap_decode(input, errors,
                    {'b': u'/', 'a': u'+'}, 'ignore')

        class IncrementalEncoder(codecs.IncrementalEncoder):

            def __init__(self, errors='strict'):
                codecs.IncrementalEncoder.__init__(self, errors)
            def encode(self, input, final=False):
                return codecs.charmap_encode(input, self.errors,
                    {'b': u'/', 'a': u'+'}, final)

        class
