import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print("my_error_handler called with %s" % exception)
    return (u'', exception.start + 1)

codecs.register_error('my_error', my_error_handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print('Encoding:', encoding)
    for text in ['abc', u'\u20ac', u'\u20acabc']:
        print('  Text:', text)
        try:
            encoded = text.encode(encoding, 'my_error')
            print('  Encoded:', encoded)
        except UnicodeEncodeError as err:
            print('  Error:', err)

# Encoding: ascii
#   Text: abc
#   Encoded: b'abc'
#   Text: €
#   Error: 'ascii' codec can't encode character '\u20ac' in position 0: ordinal not in range(128)
#   Text
