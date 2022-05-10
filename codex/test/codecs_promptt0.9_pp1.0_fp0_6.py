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

