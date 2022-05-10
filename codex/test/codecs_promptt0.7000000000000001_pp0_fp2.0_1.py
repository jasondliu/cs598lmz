import codecs
# Test codecs.register_error.

import codecs
import sys

def encoder(s):
    return s.upper(), len(s)

def decoder(s):
    return s.lower(), len(s)

