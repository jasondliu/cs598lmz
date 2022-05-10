import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print('my_error_handler:', exception)
    return ('', exception.start + 1)

codecs.register_error('test.myerror', my_error_handler)

for encoding in ['ascii', 'test.myerror']:
    print('Encoding:', encoding)
