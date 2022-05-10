import codecs
# Test codecs.register_error()

def handler(ex):
    return (u'', ex.start + 1)

codecs.register_error('test', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print encoding
    print codecs.decode('\x80', encoding, 'test')
    print codecs.decode('\xc0', encoding, 'test')
    print codecs.decode('\xff', encoding, 'test')
    print codecs.decode('\u0100', encoding, 'test')
    print codecs.decode('\U00010000', encoding, 'test')
    print codecs.decode('\U0010ffff', encoding, 'test')
    print codecs.decode('\udc80', encoding, 'test')
    print codecs.decode('\udcff', encoding, 'test')
    print codecs.decode('\ud800\udc00', encoding, 'test')
    print codecs.decode('\udbff\udfff', encoding, 'test')
    print
