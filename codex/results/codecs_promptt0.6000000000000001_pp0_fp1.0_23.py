import codecs
# Test codecs.register_error

import test.support

# The following tests require that the codecs module is importable.
# Skip them if it is not.
test.support.import_module('codecs')

def test(name, encoder_err, decoder_err, expected):
    test.support.check_warnings()
    # Test the error handler
    errh = codecs.register_error(name, encoder_err, decoder_err)
    if errh is not None:
        # Test that the error handler is actually called
        test.support.check_warnings(("register_error\(\) is a deprecated API",
                                     DeprecationWarning))
        s = 'a\x80b\x80c'
        r = codecs.encode(s, 'latin-1', name)
        if r != expected:
            raise test.support.TestFailed("%r != %r" % (r, expected))
        r = codecs.decode(s, 'latin-1', name)
        if r != expected:
            raise test.support.
