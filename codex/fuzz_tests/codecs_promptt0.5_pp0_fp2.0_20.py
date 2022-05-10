import codecs
# Test codecs.register_error

# We need a unicode error handler that raises UnicodeError

def u_error_handler(exception):
    raise UnicodeError

def test(encoding):
    try:
        codecs.lookup_error(encoding)
    except LookupError:
        pass
    else:
        print "lookup_error() didn't raise LookupError"
    codecs.register_error(encoding, u_error_handler)
    try:
        codecs.lookup_error(encoding)
    except LookupError:
        print "lookup_error() raised LookupError"
    else:
        print "lookup_error() didn't raise LookupError"

test('__test1__')
test('__test2__')
