import codecs
# Test codecs.register_error('ignore')
# Here, we set up ignore-encoding-errors to be
# the default.
codecs.register_error('ignore', codecs.ignore_errors)
# OK, let's try and decode this erroneous input.
try:
    x = "abc\xFF".decode('ascii')
except:
    print 'Unexpected error'
else:
    print 'No error'
# What if we do the same thing with UTF-8 encoding?
try:
    x = "abc\xFF".decode('utf-8')
except:
    print 'Unexpected error'
else:
    print 'No error'
