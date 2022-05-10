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
    print 'With error handler:', repr(s.decode(enc, 'ignore'))
    print 'Without error handler:', repr(s.decode(enc))
    print '-'*50

def handler(exception):
    print 'Error handler called with:', exception
    return (u'', exception.end)

codecs.register_error('test', handler)

for name in ['iso8859_7', 'cp737', 'koi8_r']:
    test(name, name)

for name in ['iso8859_7', 'cp737', 'koi8_r']:
    test(name, name + ':test')
