import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print(exception)
    return ('', exception.end)

codecs.register_error('test.myerror', handler)

def test(encoding):
    print(encoding, ':', end=' ')
    try:
        codecs.decode(b'\xff', encoding)
    except UnicodeDecodeError as e:
        print(e)

test('ascii')
test('iso8859-1')
