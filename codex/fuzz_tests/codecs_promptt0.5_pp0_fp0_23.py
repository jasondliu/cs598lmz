import codecs
# Test codecs.register_error()

def search_function(encoding):
    if encoding == 'test.notanencoding':
        return codecs.lookup('utf-8')
    return None

codecs.register_error('test.lookuperror', search_function)

def test(encoding):
    try:
        u = unicode('abc', encoding)
    except LookupError:
        print 'LookupError:', encoding
    except UnicodeError:
        print 'UnicodeError:', encoding

for encoding in ['ascii', 'test.notanencoding']:
    test(encoding)

# Test codecs.register_error()

def bad_decode(input, errors='strict'):
    raise UnicodeError(u'bad decode')

def bad_encode(input, errors='strict'):
    raise UnicodeError(u'bad encode')

codecs.register_error('test.badserror', bad_decode)
codecs.register_error('test.badencodeerror', bad_encode)

def test
