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


@skip_unless_unicode_paths
class TestUnicode(unittest.TestCase, BaseArmTest):
    def test_unicode_chars_in_filename(self):
        """
        regression test for issue #30
        """
        text_attributes = arm.TextAttributes(title=['Føksianske Tall'],
                                             authors=[arm.Author(name='Euclid')])
        with _TemporaryDirectory() as test_dir:
            n = os.path.join(test_dir, "Føkse\N{CYRILLIC CAPITAL LETTER U} vælg{0}".format(self.archive_suffix))
            _create_contents([(b"abc", text_attributes)], n)
            with self.assertRaises(arm.ArchiveError):
                statistics = arm.analyze_archive(n)


class TestPreservePaths(unittest.TestCase, BaseArmTest):
    @staticmethod
    def _get_contents(filename):
        if isinstance(
