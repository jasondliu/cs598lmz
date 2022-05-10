import codecs
# Test codecs.register_error(...) in Py2
try:
    codecs.register_error('a_test_error', 'blah')
except TypeError:
    pass
else:
    raise AssertionError("Didn't raise TypeError")

try:
    codecs.register_error('a_test_error', None)
except TypeError:
    pass
else:
    raise AssertionError("Didn't raise TypeError")

try:
    codecs.register_error('a_test_error', 'abc', 'abc')
except TypeError:
    pass
else:
    raise AssertionError("Didn't raise TypeError")

try:
    codecs.register_error('a_test_error', 'abc', 'ignore')
except TypeError:
    pass
else:
    raise AssertionErro("Didn't raise TypeError")

try:
    codecs.register_error('a_test_error', 'ignore', 'abc')
except TypeError:
    pass
else:
    raise AssertionError("Didn't raise TypeError")

