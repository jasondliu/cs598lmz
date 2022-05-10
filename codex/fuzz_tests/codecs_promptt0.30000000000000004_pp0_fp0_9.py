import codecs
# Test codecs.register_error()
#
# This test is not exhaustive.  It only tests a few error handlers.
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).
#
# (c) Copyright CNRI, All Rights Reserved. NO WARRANTY.
#
# *** Ensure that the tests don't change the default encoding ***

import test.test_support, unittest

# Error handler tests

def strict_errors(exc):
    raise exc

def ignore_errors(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (u'', exc.end)
    elif isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def replace_errors(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (u'?', exc.end)
    elif isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    else:

