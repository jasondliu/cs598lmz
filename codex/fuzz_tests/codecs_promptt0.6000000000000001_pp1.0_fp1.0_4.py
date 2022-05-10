import codecs
# Test codecs.register_error

# This should raise a LookupError because 'decode_error' is not a valid
# error handler name.
try:
    codecs.register_error('test', 'decode_error')
except LookupError:
    print('LookupError')

# This should raise a LookupError because 'test1' is not a valid error
# handler name.
try:
    codecs.register_error('test', 'test1', 'test2')
except LookupError:
    print('LookupError')

# This should raise a ValueError because 'strict' is not callable.
try:
    codecs.register_error('test', 'strict')
except ValueError:
    print('ValueError')

# This should raise a ValueError because 'test1' is not callable.
try:
    codecs.register_error('test', 'test1', 'test2')
except ValueError:
    print('ValueError')

# This should raise a ValueError because 'test2' is not callable.
try:
    codecs.register_error('
