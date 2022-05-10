import codecs
# Test codecs.register_error()

def handler(exception):
    print('Exception handler called:', exception)
    return str(exception), exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print('Encoding:', encoding)
    try:
        print(codecs.decode('\xff', encoding, 'test.lookup'))
    except Exception as e:
        print('EXCEPTION:', e)

test('ascii')
test('latin-1')
test('utf-8')
test('iso8859-1')
test('iso8859-15')
test('koi8-r')
test('cp1251')
test('cp866')
test('mbcs')
test('oem')
test('hex_codec')
test('rot_13')
test('base64_codec')
test('quopri_codec')
test('zlib_codec')
test('uu_codec')
test('bz2_codec')
test('hex_codec')
