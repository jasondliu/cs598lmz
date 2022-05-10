import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print('my_error_handler:', exception)
    return ('', exception.start + 1)

codecs.register_error('test.myerror', my_error_handler)

def test(encoding):
    print('TEST:', encoding)
    try:
        codecs.decode(b'\xff', encoding, 'test.myerror')
    except UnicodeDecodeError as e:
        print('ERROR:', e)

test('ascii')
test('latin-1')
test('iso8859-1')
test('iso8859-15')
test('iso2022_jp')
test('shift_jis')
test('euc_jp')
test('utf-8')
test('utf-16')
test('utf-32')
test('utf-16-le')
test('utf-16-be')
test('utf-32-le')
test('utf-32-be')
test('unicode-escape')
