import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    return (u'', len(input))

def bad_encode(input, errors='strict'):
    return (u'', len(input))

codecs.register_error('test.notanencoding', bad_decode)
codecs.register_error('test.notanencoding', bad_encode)

# Test that the error handler is called
