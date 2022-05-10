import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print('my_error_handler:', exception)
    return ('', exception.start + 1)

codecs.register_error('test.myerror', my_error_handler)

for encoding in ['latin_1', 'ascii', 'test.myerror']:
    print('Encoding  :', encoding)
    print('Encoding  :', 'abcdefghijklmnop', '->', codecs.encode('abcdefghijklmnop', encoding))
    print('Decoding  :', b'abcdefghijklmnop', '->', codecs.decode(b'abcdefghijklmnop', encoding))
    print('Encoding  :', '\x80', '->', codecs.encode('\x80', encoding))
    print('Decoding  :', b'\x80', '->', codecs.decode(b'\x80', encoding))
    print('Encoding  :', '\u1234', '->', codecs
