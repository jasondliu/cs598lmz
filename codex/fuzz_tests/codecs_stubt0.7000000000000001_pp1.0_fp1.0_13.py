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

# ############################################################################
# ############################################################################

if __name__ == "__main__":

    import unittest
    import sys

    sys.path.insert(0, ".")
    from test import test_support

    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(TestEncoding))
    suite.addTest(unittest.makeSuite(TestDecoding))

    test_support.run_suite(suite)
