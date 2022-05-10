import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print 'my_error_handler:', exception
    return (u'\ufffd', exception.end)

def test(codec):
    print '-'*50
    print codec
    text = u'pi: \u03c0'
    print 'INPUT :', repr(text)
    encoded = codec.encode(text, 'replace')[0]
    print 'REPLACED:', repr(encoded)
    codecs.register_error('test.replace', my_error_handler)
    encoded = codec.encode(text, 'test.replace')[0]
    print 'CUSTOM :', repr(encoded)
    print

for codec in ['ascii', 'latin-1', 'utf-8']:
    test(codec)

print '-'*50
