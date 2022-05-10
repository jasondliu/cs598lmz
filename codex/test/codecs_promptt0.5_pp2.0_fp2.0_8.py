import codecs
# Test codecs.register_error

import codecs

def search_function(encoding):
    if encoding != 'test.searchfunction':
        return None
    return codecs.CodecInfo(
        name='test.searchfunction',
        encode=lambda x, y: x,
        decode=lambda x, y: x,
    )

codecs.register(search_function)

