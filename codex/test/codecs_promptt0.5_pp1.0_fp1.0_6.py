import codecs
# Test codecs.register_error
import sys
import os

def search_function(encoding):
    if encoding == 'toto':
        return codecs.CodecInfo(
            name='toto',
            encode=lambda x,y: (b'', 0),
            decode=lambda x,y: ('', 0),
            incrementalencoder=None,
            incrementaldecoder=None,
            streamreader=None,
            streamwriter=None,
        )
    return None

codecs.register(search_function)

# Test codecs.lookup
assert codecs.lookup('toto')

# Test codecs.lookup_error

def handle_error(exception):
    return ('', 0)

assert codecs.lookup_error('strict')
assert codecs.lookup_error('ignore')
assert codecs.lookup_error('replace')
