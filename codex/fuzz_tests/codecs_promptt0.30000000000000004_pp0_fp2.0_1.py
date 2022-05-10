import codecs
# Test codecs.register_error()

def handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('test.xmlcharrefreplace', handler)

for encoding in ('ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32'):
    print '%s:' % encoding
    print ' ',
    try:
        print repr(unicode('<\u1234>', encoding, 'test.xmlcharrefreplace'))
    except UnicodeError, err:
        print 'ERROR:', err
    print ' ',
    try:
        print repr(unicode('<\u1234>', encoding, 'xmlcharrefreplace'))
    except UnicodeError, err:
        print 'ERROR:', err
    print ' ',
    try:
        print repr(unicode('<\u1234>', encoding, 'strict'))
    except UnicodeError, err:
        print 'ERROR:', err
    print ' ',
    try:
        print repr(unicode('<\u1234>', encoding
