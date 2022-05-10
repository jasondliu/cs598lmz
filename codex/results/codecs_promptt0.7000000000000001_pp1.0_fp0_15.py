import codecs
# Test codecs.register_error
import string

def uchr(i):
    return unichr(i)

def main():
    # Try with a non-unicode error handler
    try:
        codecs.register_error(str, codecs.replace_errors)
    except TypeError:
        pass
    else:
        print 'error did not occur'

    # Try with a non-callable error handler
    try:
        codecs.register_error('ascii', 'foo')
    except TypeError:
        pass
    else:
        print 'error did not occur'

    # Try with an invalid name
    try:
        codecs.register_error('foo', codecs.replace_errors)
    except LookupError:
        pass
    else:
        print 'error did not occur'

    # Try with a valid replacement error handler
    try:
        codecs.register_error('ascii', codecs.replace_errors)
    except:
        print 'Unexpected error'
    else:
        # Check the registered error handler
        try:
            print '
