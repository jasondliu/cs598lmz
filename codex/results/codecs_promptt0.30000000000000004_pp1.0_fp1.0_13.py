import codecs
# Test codecs.register_error()

import codecs

def my_error(exception):
    print('my_error:', exception)
    return (u'', exception.start + 1)

codecs.register_error('test.my_error', my_error)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print('Encoding:', encoding)
    try:
        print(codecs.decode('abc\xFFdef', encoding, 'test.my_error'))
    except UnicodeDecodeError as e:
        print('ERROR:', e)
    print()

# Encoding: ascii
# my_error: 'ascii' codec can't decode byte 0xff in position 3: ordinal not in range(128)
# abcdef
#
# Encoding: latin-1
# my_error: 'latin-1' codec can't decode byte 0xff in position 3: ordinal not in range(256)
# abcdef
#
# Encoding: utf-8
# my_error: '
