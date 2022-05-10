import codecs
# Test codecs.register_error('test', codecs.replace_errors)
# codecs.register_error('test', codecs.ignore_errors)
# codecs.register_error('test', codecs.xmlcharrefreplace_errors)
# codecs.register_error('test', codecs.backslashreplace_errors)

def test(encoding):
        print '-'*50
        print 'Encoding :', encoding
        print 'INPUT    :', unicode(INPUT, encoding, 'test')
        print 'ENCODING :', unicode(INPUT, encoding, 'test').encode(encoding, 'test')

for encoding in ('utf-8', 'ascii', 'latin-1', 'iso-8859-1', 'iso-8859-15'):
        test(encoding)
