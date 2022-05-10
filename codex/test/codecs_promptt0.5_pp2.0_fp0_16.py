import codecs
# Test codecs.register_error()

def search_function(encoding):
    if encoding == 'test.unicode.replace':
        return codecs.lookup('unicode_internal')
    return None

codecs.register(search_function)

def test():
    s = '\xff'
