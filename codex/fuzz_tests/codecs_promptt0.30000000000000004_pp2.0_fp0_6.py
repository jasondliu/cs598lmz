import codecs
# Test codecs.register_error
# This test is not exhaustive.

# Test the first argument of register_error

# This should fail
try:
    codecs.register_error(None, lambda x: x)
except TypeError:
    pass
else:
    print('Failed to raise TypeError')

# This should fail
try:
    codecs.register_error(lambda x: x, lambda x: x)
except TypeError:
    pass
else:
    print('Failed to raise TypeError')

# This should fail
try:
    codecs.register_error(1, lambda x: x)
except TypeError:
    pass
else:
    print('Failed to raise TypeError')

# This should fail
try:
    codecs.register_error('strict', lambda x: x)
except LookupError:
    pass
else:
    print('Failed to raise LookupError')

# Test the second argument of register_error

# This should fail
try:
    codecs.register_error('test', None)
except TypeError:
    pass

