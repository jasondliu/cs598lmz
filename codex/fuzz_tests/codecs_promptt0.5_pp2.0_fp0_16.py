import codecs
# Test codecs.register_error()

def search_function(encoding):
    if encoding == 'test.unicode.replace':
        return codecs.lookup('unicode_internal')
    return None

codecs.register(search_function)

def test():
    s = '\xff'
    for errors in ['strict', 'replace', 'ignore', 'test.unicode.replace']:
        print errors, repr(s.decode('latin-1', errors))

test()

# Test codecs.lookup_error()

def my_error(exception):
    print 'my_error:', exception

codecs.lookup_error('test.my_error')
codecs.lookup_error('test.my_error')(my_error)

def test():
    s = '\xff'
    for errors in ['strict', 'replace', 'ignore', 'test.my_error']:
        print errors, repr(s.decode('latin-1', errors))

test()
