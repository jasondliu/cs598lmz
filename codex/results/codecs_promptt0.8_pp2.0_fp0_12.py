import codecs
# Test codecs.register_error().

from test_support import TestSkipped, run_unittest, import_module


class TestRegisterError(unittest.TestCase):
    error_handler_tests = [
        ('xmlcharrefreplace', '\u1234\u5678', '&#4660;&#22136;'),
        ('backslashreplace', '\u1234\u5678', '\\u1234\\u5678'),
        ('namereplace', '\u1234\u5678', '\\N{DEVANAGARI LETTER QA}\\N{CYRILLIC CAPITAL LETTER ABKHASIAN DZE}'),
        ('strict', '\u1234\u5678', None),
        ]

    def setUp(self):
        self.unicode_string = '\u1234\u5678'
        self.byte_string = '\xe1\x88\xb4\xe5\x99\xb8'
        self.encoding = 'utf-8'

    def tearDown(self):
        codecs.register_
