import codecs
# Test codecs.register_error('strict')

# unicode data
u = chr(0xC4) + chr(0xF6) + chr(0xE4) + chr(0xF6) + chr(0xFC)

# iso-8859-1 encoding
s = u.encode('iso-8859-1')

try:
    # try to decode with the default error handler
    print(s.decode('iso-8859-1'))
except UnicodeDecodeError as e:
    # but it fails
    print('ERROR:', e)

# register a new error handler
codecs.register_error('strict', codecs.strict_errors)

try:
    # try to decode with the strict error handler
    print(s.decode('iso-8859-1', 'strict'))
except UnicodeDecodeError as e:
    # but it fails
    print('ERROR:', e)

# register a new error handler
codecs.register_error('ignore', codecs.ignore_errors)

# try
