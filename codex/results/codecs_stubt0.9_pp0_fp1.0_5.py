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

from encodedecodefiles import open_test_file, open_test_textfile, \
     EncodeTestHelper, DecodeTestHelper

class EncodeTest(EncodeTestHelper, unittest.TestCase):
    encoding = "utf-16"
    testfile_unencoded = "utf8.txt"

class EncodeTestUTF16LE(EncodeTest, unittest.TestCase):
    encoding = "utf-16-le"
    testfile_encoded = "encoded/utf16le.txt"

class EncodeTestUTF16BE(EncodeTest, unittest.TestCase):
    encoding = "utf-16-be"
    testfile_encoded = "encoded/utf16be.txt"

class EncodeTestUTF16Exotic(EncodeTest, unittest.TestCase):
    encoding = "utf-16-exotic"
    testfile_encoded = "encoded/utf16exotic.txt"

class EncodeTestUTF16Platform(EncodeTest, unittest.TestCase):
    encoding =
