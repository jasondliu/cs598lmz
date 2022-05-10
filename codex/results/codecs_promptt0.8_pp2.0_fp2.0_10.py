import codecs
# Test codecs.register_error
def handler1(exception):
    return ("BAD", exception.end)

codecs.register_error('test.name1', handler1)

# "ignore" is special
codecs.register_error('test.name2', 'ignore')

# Unregister
codecs.register_error('test.name1', None)
codecs.register_error('test.name2', None)

# Test that unregistered "ignore" still works
s = "\udcec\udcec\udcec"
s.encode("ascii", "ignore")
# Test that unregistered handler raises error

try:
    s.encode('ascii', 'test.name1')
except LookupError:
    pass
else:
    print("Expected LookupError")
