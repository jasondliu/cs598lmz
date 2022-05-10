import codecs
# Test codecs.register_error()

import codecs

def search_function(encoding):
    if encoding == 'test.unknown-error':
        return codecs.lookup('test.strict-error')

codecs.register_error('test.unknown-error', search_function)

