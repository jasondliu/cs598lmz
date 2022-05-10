import codecs
# Test codecs.register_error()

def search_function(encoding):
    if encoding == 'test.notanencoding':
        return codecs.lookup('utf-8')
    return None
codecs.register(search_function)

def encoding_error_handler(*args):
    raise UnicodeError, "test error handler"

data = u'\u2200'
try:
    codecs.decode(data, 'test.notanencoding')
except UnicodeError:
    print 'OK'
try:
    codecs.decode(data, 'test.notanencoding', encoding_error_handler)
except UnicodeError, exc:
    p
