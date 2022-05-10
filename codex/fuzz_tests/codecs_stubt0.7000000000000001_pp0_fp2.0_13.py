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

def test_unicode_error(self):
    INVALID_UTF8 = b'\xff'
    INVALID_UTF16 = b'\xff\xfe'
    INVALID_UTF32 = b'\xff\xfe\x00\x00'
    # RE_DECODE_ERROR is different on Python 3.
    RE_DECODE_ERROR = re.compile(
        r"^(?:UnicodeDecodeError|decode error): (?:[^:]+: )?(.*)$")
    with self.assertRaisesRegex(UnicodeDecodeError,
                                RE_DECODE_ERROR,
                                msg="Invalid UTF-8") as cm:
        INVALID_UTF8.decode('utf-8')
    self.assertEqual(cm.exception.reason, "invalid continuation byte")
    self.assertEqual(cm.exception.start, 0)
    self.assertEqual(cm.exception.end, 1)
    self.assertEqual(cm.exception.object, IN
