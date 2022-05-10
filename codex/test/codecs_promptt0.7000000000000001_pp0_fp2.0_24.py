import codecs
# Test codecs.register_error, as well as incremental encoding and decoding.

# Encoding
def search_function(encoding):
    if encoding == 'test.unicode':
        return codecs.getincrementalencoder('UTF-8'), None
codecs.register(search_function)

def search_function(encoding):
    if encoding == 'test.unicode':
        return codecs.getincrementaldecoder('UTF-8'), None
codecs.register(search_function)

def search_function(encoding):
    if encoding == 'test.unicode':
        return codecs.getencoder('UTF-8'), None
codecs.register(search_function)

def search_function(encoding):
    if encoding == 'test.unicode':
        return codecs.getdecoder('UTF-8'), None
codecs.register(search_function)

def search_function(encoding):
    if encoding == 'test.unicode':
        return codecs.getreader('UTF-8'), None
codecs.register(search_function)

