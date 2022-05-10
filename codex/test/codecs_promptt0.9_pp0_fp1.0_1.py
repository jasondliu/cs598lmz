import codecs
# Test codecs.register_error
import sys
import types
import weakref

# Test codecs.encode w/ errors
def test_main():
    #
    # register_error()

    #
    # Start with a custom class
    #
    class ThisClass:
        pass
    ThisClass.__name__ = 'ThisClass'
    o = ThisClass()
    o.__name__ = 'ThisClass.__call__'
    def searchfunc(encoding):
        if encoding in ('test.notfound', 'test.unknown'):
            return None
        if encoding == 'test.replace':
            return codecs.replace_errors
        return o
    codecs.register_error('test', searchfunc)
    #
    # Check all search functions are tried if none succeed
    #
    try:
        codecs.lookup_error('test')
    except LookupError:
        pass
    else:
        raise TestFailed("did not raise exception for notfound error handler name")
    #
    # Test a module-level function is wrapped
    #
