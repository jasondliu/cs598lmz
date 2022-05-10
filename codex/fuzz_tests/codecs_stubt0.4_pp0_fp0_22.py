import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

#
# Test that the default error handler is not called
#

def test_default_error_handler():
    # This is a bit tricky, as the default error handler
    # is not called when the codec is registered with
    # the codecs module.
    #
    # The following codecs are expected to raise an
    # UnicodeEncodeError:
    #
    # - 'ascii'
    # - 'iso-8859-1'
    # - 'iso-8859-15'
    # - 'iso-8859-2'
    # - 'iso-8859-3'
    # - 'iso-8859-4'
    # - 'iso-8859-5'
    # - 'iso-8859-6'
    # - 'iso-8859-7'
    # - 'iso-8859-8'
    # - 'iso-8859-9'
    # - 'iso-8859-10'
    # - 'iso-8859-13'
    # - 'iso-8859-14'
    #
