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

# Test that the codecs module is sane
class CodecsModuleTest(unittest.TestCase):

    def test_encode_decode_error_handler(self):
        # Check that the error handler is called with the correct
        # number of parameters and that the parameters have the correct
        # types

        # This is the list of all codecs that support the 'surrogateescape'
        # error handler (which is the only one we are going to test).
        # We are going to test them all with the same input string, which
        # is the UTF-8 encoding of the Unicode string "\udcff\udcfe".
        # As this string is not valid UTF-8, it should always trigger
        # the error handler.
        codecs_to_test = [
            "ascii", "big5", "big5hkscs", "cp037", "cp424", "cp437", "cp500",
            "cp720", "cp737", "cp775", "cp850", "cp852", "cp855", "cp856",
            "cp8
