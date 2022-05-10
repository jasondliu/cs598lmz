import codecs
# Test codecs.register_error()

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

def codec_error_handler(exception):
    return ('', exception.end)

codecs.register(search_function)
codecs.register_error('test.searchfunction', codec_error_handler)

try:
    u'\U0010FFFF'.encode('test.searchfunction')
except UnicodeEncodeError as e:
    print(e)

# Test codecs.register_error() with unicode_error

import codecs

def codec_error_handler(exception):
    return ('', exception.end)

codecs.register_error('test.unicode_error', codec_error_handler)

try:
    u'\U0010FFFF'.encode('ascii', 'test.unicode_error')
except UnicodeEncodeError as e:
    print(e)

# Test codecs.register_error() with unicode
