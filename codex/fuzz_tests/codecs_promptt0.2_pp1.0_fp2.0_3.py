import codecs
# Test codecs.register_error

import codecs

def test(name, enc):
    print '-'*50
    print 'Encoding:', enc
    print 'Codec:', name
    print '-'*50
    print 'Encoding...'
    u = u'pi: \u03c0'
    s = u.encode(enc)
    print 'Original:', repr(s)
    print 'Errorhandler:', codecs.lookup_error(name)
    print 'Encoded :', repr(s.encode(enc, name))
    print 'Decoding...'
    print 'Original:', repr(s.decode(enc))
    print 'With errorhandler:', repr(s.decode(enc, name))

test('ignore', 'ascii')
test('replace', 'ascii')
test('xmlcharrefreplace', 'ascii')
test('backslashreplace', 'ascii')
test('namereplace', 'ascii')

test('ignore', 'latin-1')
test('replace', 'latin-1')
test('
