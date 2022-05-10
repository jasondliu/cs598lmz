import codecs
# Test codecs.register_error
#
# This has been tested on CPython 2.1 and 2.2, on a PC

import codecs
import string

# a simple replacement_error

class my_error (Exception):
    def __init__ (self, object, start, end, reason):
        self.object = object
        self.start = start
        self.end = end
        self.reason = reason

    def __str__ (self):
        return "error %s at position %d-%d" % (self.reason,
                                               self.start, self.end)

# a simple error handler

def my_error_handler (errors):
    raise my_error (errors.object, errors.start, errors.end,
                    'my_error_handler')

# a simple encoder

class my_encoder (codecs.Codec):
    def encode (self, a, errors='strict'):
        return a.upper()

# a simple decoder

