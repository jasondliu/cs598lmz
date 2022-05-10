import codecs
# Test codecs.register_error
try:
    codecs.register_error('test.ignore', codecs.ignore_errors)
except TypeError:
    pass
else:
    print('FAILED: codecs.register_error did not raise TypeError')
# Test codecs.lookup_error
try:
    codecs.lookup_error('test.ignore')
except LookupError:
    pass
else:
    print('FAILED: codecs.lookup_error did not raise LookupError')
try:
    codecs.lookup_error('test.ignore')
except LookupError:
    pass
else:
    print('FAILED: codecs.lookup_error did not raise LookupError')
try:
    codecs.lookup_error('test.ignore')
except LookupError:
    pass
else:
    print('FAILED: codecs.lookup_error did not raise LookupError')
# Test codecs.register_error
try:
    codecs.register_error('test.ignore', lambda x: (u'', x))
except TypeError
