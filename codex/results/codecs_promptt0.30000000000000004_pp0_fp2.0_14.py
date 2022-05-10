import codecs
# Test codecs.register_error()

def handler(exception):
    print('Exception:', exception)
    return '<exception>', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print('Encoding:', encoding)
    text = 'pi: \u03c0'
    print('Original:', text)
    encoded = text.encode(encoding, 'test.lookup')
    print('Encoded :', encoded)
    decoded = encoded.decode(encoding, 'test.lookup')
    print('Decoded :', decoded)
    print()

test('ascii')
test('latin-1')
test('utf-8')
test('utf-16')
test('utf-32')

# Encoding: ascii
# Original: pi: π
# Exception: 'ascii' codec can't encode character '\u03c0' in position 4: ordinal not in range(128)
# Encoded : b'pi: <exception>'
# Exception: '
