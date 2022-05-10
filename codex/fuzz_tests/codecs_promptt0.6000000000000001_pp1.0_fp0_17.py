import codecs
# Test codecs.register_error

def handler_function(exception):
    return ("?", exception.start + 1)

codecs.register_error("test.xlate", handler_function)

# codecs.lookup_error('strict') should return a function
# (in this case, the strict handler)
if not hasattr(codecs.lookup_error('strict'), '__call__'):
    raise TestFailed, "lookup_error('strict') should return a function"

# the codecs module should be set up with error handlers for
# all the standard encodings
for encoding in ['ascii', 'latin-1', 'utf-8', 'iso2022_jp']:
    try:
        codecs.lookup_error(encoding)
    except LookupError:
        print 'Error handler for %s not found' % encoding
        raise TestFailed

# registering an error handler twice should raise a LookupError
try:
    codecs.register_error("test.xlate", handler_function)
except LookupError:
    pass
else
