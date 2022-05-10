import codecs
# Test codecs.register_error for when you want to error out on an encoding error

import pytest

def FIXME_test_codecs_track_errors():
    import codecs
    def my_handler(exc):
        return u"*IGNORE*", 6
    with pytest.raises(UnicodeDecodeError):
        codecs.register_error("my_error_handler", my_handler)
        codecs.decode(b"\xff", "ascii", "my_error_handler")
    codecs.register_error("ignore", codecs.ignore_errors)
    assert codecs.decode(b"\xff", "ascii", "ignore") == u"\ufffd"

def test_decode_recover_from_errors():
    # Python cannot recover from a decoding error.
    # The best it can do is tell you where in the string it errored out.
    # But you can use the codecs module to recover from errors in a more elegant manner
    import codecs
    def my_handler(exc):
        return u"*IGNORE*", 5
