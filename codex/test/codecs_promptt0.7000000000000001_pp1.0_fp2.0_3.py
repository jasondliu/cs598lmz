import codecs
# Test codecs.register_error
def lookup(name):
    print('lookup:', name)
    return codecs.lookup_error(name)

# Register the error handler under a new name
codecs.register_error('test.lookup', lookup)

# Encode a string with 'replace' error handling and
# look up the error handler
s = 'spam'
try:
    print(s.encode('ascii', 'test.lookup'))
except UnicodeEncodeError as err:
    print('ERROR:', err)
# Test codecs.register_error
def replace(err):
    print('replace:', err)
    return '?', err.start + 1

# Register the error handler under a new name
codecs.register_error('test.replace', replace)

# Encode a string with 'replace' error handling and
# look up the error handler
s = 'spam'
try:
    print(s.encode('ascii', 'test.replace'))
except UnicodeEncodeError as err:
    print('ERROR:', err)

