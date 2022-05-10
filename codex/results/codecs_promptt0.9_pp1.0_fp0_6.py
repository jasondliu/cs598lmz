import codecs
# Test codecs.register_error function

import codecs

def handle_codecs_error(exc):
    # Since this is registered as the "backup error handler" (the second
    # argument to register_error) it will only be invoked on a
    # LookupError.
    if isinstance(exc, LookupError):
        print('LookupError: %s' % exc.args)
        return (u'SORRY', exc.end)
    else:
        raise exc

encoder = codecs.getencoder('test.test_codecs.test_register_error')
encoder(u'test', handle_codecs_error)

encoder = codecs.getencoder('test.test_codecs.test_register_error2')
try:
    encoder(u'test', handle_codecs_error)
    self.fail('LookupError not raised')
except LookupError as e:
    print(e)

# We do not test the full functionality of codecs.register_error because the
# regression test suite does not have the necessary interface
