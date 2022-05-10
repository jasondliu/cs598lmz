import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('my_error_handler', my_error_handler)

# Encoding

print '\nEncoding:'

for encoding in ['ascii', 'my_error_handler']:
    print '\nEncoding with %s:' % encoding
    print codecs.encode('abc\u3042\u3044', encoding)

# Decoding

print '\nDecoding:'

for encoding in ['ascii', 'my_error_handler']:
    print '\nDecoding with %s:' % encoding
    print codecs.decode('abc\x80\x81', encoding)
