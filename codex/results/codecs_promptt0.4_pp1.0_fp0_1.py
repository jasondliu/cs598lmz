import codecs
# Test codecs.register_error

# This test should cause a LookupError to be raised.
try:
    codecs.register_error('nonexistent', None)
except LookupError:
    pass
else:
    print('LookupError not raised')

# This test should cause a TypeError to be raised.
try:
    codecs.register_error(None, None)
except TypeError:
    pass
else:
    print('TypeError not raised')

# This test should cause a TypeError to be raised.
try:
    codecs.register_error('test', None)
except TypeError:
    pass
else:
    print('TypeError not raised')

# This test should cause a TypeError to be raised.
try:
    codecs.register_error('test', 'test')
except TypeError:
    pass
else:
    print('TypeError not raised')

# This test should cause a TypeError to be raised.
try:
    codecs.register_error('test', lambda x, y, z: None)
except TypeError:
    pass
else:

