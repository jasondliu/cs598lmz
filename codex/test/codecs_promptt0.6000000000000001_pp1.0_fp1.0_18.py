import codecs
# Test codecs.register_error()

# This error handler replaces all characters in the range U+DC80..U+DCFF
# by '?' characters.  This is used to test if the codecs module passes
# the correct start and end argument to the error handler.

def my_error_handler(exception):
    if not isinstance(exception, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exception)
    print ('my_error_handler: encoding=%r, start=%r, end=%r' %
           (exception.encoding, exception.start, exception.end))
    return ('?' * (exception.end - exception.start),
            exception.end)

codecs.register_error('test.dc80', my_error_handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print (encoding, ':', end=' ')
