import codecs
# Test codecs.register_error().

# Use codecs.lookup_error() to check what error handler is set.

def print_error(name):
    print '%s: %s' % (name, codecs.lookup_error(name))

# Register a new error handler
def ignore_error1(exception):
    return (u'', exception.end)
codecs.register_error('ignore1', ignore_error1)

# Register another error handler
def ignore_error2(exception):
    return (u'', exception.end+1)
codecs.register_error('ignore2', ignore_error2)

print_error('strict')
print_error('ignore')
print_error('replace')
print_error('xmlcharrefreplace')
print_error('backslashreplace')
print_error('namereplace')
print_error('ignore1')
print_error('ignore2')

# Deregister one of the error handlers again
codecs.register_error('ignore2', None)
print_error('ignore2')

# Register a new
