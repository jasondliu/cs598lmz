import codecs
# Test codecs.register_error('test', test_error)
def test_error(exc):
    print(exc)
    return (u'\ufffd', exc.start + 1)
codecs.register_error('test', test_error)

s = u'\u00a0'
encoded = s.encode('ascii', 'test')
print(repr(encoded))

# Test codecs.register_error('test', None)
codecs.register_error('test', None)

try:
    encoded = s.encode('ascii', 'test')
except Exception as e:
    print(e)

# Test codecs.register_error('test', test_error)
codecs.register_error('test', test_error)

# Test codecs.lookup_error('test')
print(codecs.lookup_error('test'))

# Test codecs.lookup_error('missing')
try:
    codecs.lookup_error('missing')
except Exception as e:
    print(e)

# Test
