import codecs
# Test codecs.register_error()

import codecs

# This codec uses the default encoding error handler
def search_function(encoding):
    if encoding != 'test.searchfunction':
        return None
    utf8 = codecs.lookup('utf-8')
    return codecs.CodecInfo(
        name='test.searchfunction',
        encode=utf8.encode,
        decode=utf8.decode,
        incrementalencoder=utf8.incrementalencoder,
        incrementaldecoder=utf8.incrementaldecoder,
        streamreader=utf8.streamreader,
        streamwriter=utf8.streamwriter,
    )

codecs.register(search_function)

# This codec uses a custom encoding error handler
def search_function(encoding):
    if encoding != 'test.searchfunction2':
        return None
    utf8 = codecs.lookup('utf-8')
    def custom_decode(input, errors='strict'):
        return utf8.decode(input, errors), len(input)
    return codecs.
