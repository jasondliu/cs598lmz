import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print('my_error_handler:', exception)
    return ('', exception.end)

codecs.register_error('test.myerror', my_error_handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print('Encoding:', encoding)
    print(codecs.decode('\xff', encoding, 'test.myerror'))
    print(codecs.decode('\xff\xff', encoding, 'test.myerror'))
    print(codecs.decode('\xff\xff\xff', encoding, 'test.myerror'))
    print(codecs.decode('\xff\xff\xff\xff', encoding, 'test.myerror'))
    print()

# Test codecs.register_error() with a function

import codecs

def my_error_handler(exception):
    print('my_error_handler:', exception)
    return ('', exception.end)

