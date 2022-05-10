import codecs
# Test codecs.register_error

def bad_decode(input, errors='strict'):
    return (u'', len(input))

codecs.register_error('test.notanencoding', bad_decode)

# Encode to an encoding that doesn't exist
try:
    'test'.encode('notanencoding')
except LookupError:
    pass
else:
    print('LookupError expected')

# Decode from an encoding that doesn't exist
try:
    b'test'.decode('notanencoding')
except LookupError:
    pass
else:
    print('LookupError expected')

# Encode to an encoding that exists, but has a bad_encode()
try:
    'test'.encode('test.notanencoding')
except UnicodeEncodeError:
    pass
else:
    print('UnicodeEncodeError expected')

# Decode from an encoding that exists, but has a bad_decode()
try:
    b'test'.decode('test.notanencoding')
except UnicodeDecodeError:
