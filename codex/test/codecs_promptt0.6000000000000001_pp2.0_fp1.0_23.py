import codecs
# Test codecs.register_error() handler
import sys
def handler(exception):
    print('[{}]'.format(exception.__class__.__name__), end=' ')
    return '', exception.end
codecs.register_error('test.handler', handler)
for encoding in ['ascii', 'iso8859-1', 'utf-8']:
    print(encoding, ':', end=' ')
    print(codecs.decode(b'\x80stuff', encoding, 'test.handler'), end=' ')
    print(codecs.decode(b'\x80stuff', encoding, 'ignore'), end=' ')
    print(codecs.decode(b'\x80stuff', encoding, 'replace'), end=' ')
    print(codecs.decode(b'\x80stuff', encoding, 'backslashreplace'), end=' ')
