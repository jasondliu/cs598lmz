import codecs
# Test codecs.register_error()

def search_function(encoding):
    if encoding == 'test.notanencoding':
        return codecs.lookup('utf-8')
    return None

codecs.register_error('test.lookuperror', search_function)

