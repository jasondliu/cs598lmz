import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    if isinstance(exception, UnicodeDecodeError):
        print('UnicodeDecodeError')
        return ('', exception.start + 1)
    else:
        print('Other error')
        return ('', exception.start)

codecs.register_error('test.myerror', my_error_handler)

# Test with UnicodeDecodeError
print(codecs.decode('\xff', 'ascii', 'test.myerror'))

# Test with other error
print(codecs.decode('\xff', 'ascii', 'test.myerror'))
