import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print('my_error_handler:', exception)
    return ('', exception.start + 1)

codecs.register_error('test.myerror', my_error_handler)

for encoding in ['ascii', 'test.myerror']:
    print('Encoding:', encoding)
    try:
        codecs.decode('\xff', encoding)
    except UnicodeDecodeError as err:
        print('ERROR:', err)
    print()

# Encoding: ascii
# ERROR: 'ascii' codec can't decode byte 0xff in position 0: ordinal not in range(128)
#
# Encoding: test.myerror
# my_error_handler: 'test.myerror' codec can't decode byte 0xff in position 0: ordinal not in range(128)
# ERROR: 'test.myerror' codec can't decode byte 0xff in position 1: ordinal not in range(128)
