import codecs
# Test codecs.register_error()

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('rot_13')
    return None

codecs.register(search_function)

