import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):
    def test_convert(self):
        self.assertEquals(convert('abc'), 'abc')
        self.assertEquals(convert('abc\x80'), 'abc\uFFFD')
        self.assertEquals(convert('abc\x80def'), 'abc\uFFFDdef')
        self.assertEquals(convert('abc\x80def\x80'), 'abc\uFFFDdef\uFFFD')
        self.assertEquals(convert('abc\x80def\x80ghi'), 'abc\uFFFDdef\uFFFDghi')
        self.assertEquals(convert('abc\x80def\x80ghi\x80'), 'abc\uFFFDdef\uFFFDghi\uFFFD')
        self.assertEquals(convert('abc\x80def\x80ghi\x80jkl'), 'abc\uFFFDdef\uFFFDghi\uFFFDjkl')

