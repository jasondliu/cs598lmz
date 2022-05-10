import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test', handler)

# Test a simple codec

import codecs

def test_search_function(encoding):
    if encoding != 'test':
        return None
    codec = codecs.CodecInfo(
        name='test',
        encode=lambda input, errors: (u'', len(input)),
        decode=lambda input, errors: (u'', len(input)),
        incrementalencoder=None,
        incrementaldecoder=None,
        streamreader=None,
        streamwriter=None,
    )
    return codec

codecs.register(test_search_function)

# Test a simple codec with a simple incremental encoder

import codecs

def test_search_function(encoding):
    if encoding != 'test':
        return None
