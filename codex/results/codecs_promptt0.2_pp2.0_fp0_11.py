import codecs
# Test codecs.register_error

import codecs

def test(encoding):
    print '-'*50
    print 'Encoding :', encoding
    print '-'*50
    print 'Default:'
    try:
        u'\u3042\u3044'.encode(encoding)
    except UnicodeEncodeError, err:
        print 'ERROR:', err
    print
    print 'XMLcharrefreplace:'
    try:
        u'\u3042\u3044'.encode(encoding, 'xmlcharrefreplace')
    except UnicodeEncodeError, err:
        print 'ERROR:', err
    print
    print 'Ignore:'
    try:
        u'\u3042\u3044'.encode(encoding, 'ignore')
    except UnicodeEncodeError, err:
        print 'ERROR:', err
    print
    print 'Replace:'
    try:
        u'\u3042\u3044'.encode(encoding, 'replace')
    except UnicodeEncodeError, err:
        print 'ERROR:', err
    print

