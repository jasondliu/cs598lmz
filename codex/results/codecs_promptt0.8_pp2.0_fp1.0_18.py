import codecs
# Test codecs.register_error

import test.test_support, unittest
import codecs, sys, StringIO

# A codec that raises an error if decoding a certain substring, decoding
# another substring to a different error, and ignoring decoding
# everything else.

class Codec(codecs.Codec):

    def encode(self, input, errors='strict'):
        return codecs.utf_8_encode(input, errors)

    def decode(self, input, errors='strict'):
        if input.find('\x00') >= 0:
            m = codecs.lookup_error('test.codece')
            res = u''.join(m(u'\ufffd')(c) for c in input)
        elif input.find('\xff') >= 0:
            m = codecs.lookup_error('test')
            res = u''.join(m(u'\ufffe')(c) for c in input)
        else:
            res = input.decode('ascii')
        return (res, len(input))

codecs.
