import codecs
# Test codecs.register_error()

import codecs
import sys

def search_function(encoding):
    print 'search_function:', encoding
    if encoding == 'test.unicode':
        return codecs.getregentry('test_unicode')
    return None

def test_unicode_encode(input, errors='strict'):
    print 'test_unicode_encode:', input, errors
    return (u'XXX', len(input))

def test_unicode_decode(input, errors='strict'):
    print 'test_unicode_decode:', input, errors
    return (u'XXX', len(input))

codecs.register(search_function)

class Test:
    def test_encode(self):
        u = u'abc'
        for errors in ['strict', 'replace', 'ignore', 'xmlcharrefreplace',
                       'backslashreplace', 'namereplace']:
            print 'errors:', errors
            self.assertEqual(u.encode('test.unicode', errors), 'XXX')
           
