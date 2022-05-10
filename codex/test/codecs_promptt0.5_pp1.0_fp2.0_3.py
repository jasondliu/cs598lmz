import codecs
# Test codecs.register_error
#
# This test should be run with the -u command line option.

print('TEST:', codecs.register_error.__name__)

print('TEST: error handling')

def my_error1(exc):
    if isinstance(exc, UnicodeDecodeError):
        print('my_error1 called with', exc.object[exc.start:exc.end])
        return (u'', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def my_error2(exc):
    if isinstance(exc, UnicodeDecodeError):
        print('my_error2 called with', exc.object[exc.start:exc.end])
        return (u'@', exc.end+1)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def my_error3(exc):
    if isinstance(exc, UnicodeDecodeError):
        print('my_error3 called with', exc.object[exc.start:exc.end])
       
