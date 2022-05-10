import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad decode"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad encode"

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

for encoding in ('ascii', 'latin-1', 'utf-8'):
    try:
        u = unicode('abc', encoding, 'test.bad_decode')
    except UnicodeError, err:
        print "OK:", err
    else:
        print "encoding", encoding, "should have failed"

for encoding in ('ascii', 'latin-1', 'utf-8'):
    try:
        s = u'abc'.encode(encoding, 'test.bad_encode')
    except UnicodeError, err:
        print "OK:", err
    else:
        print "encoding", encoding
