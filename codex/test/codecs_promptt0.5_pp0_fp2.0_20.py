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
