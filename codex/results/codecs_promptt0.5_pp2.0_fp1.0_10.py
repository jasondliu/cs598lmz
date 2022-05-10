import codecs
# Test codecs.register_error("test.xmlcharrefreplace", xmlcharrefreplace)
# Test codecs.register_error("test.backslashreplace", backslashreplace)

class Test_XMLCharRefReplace(unittest.TestCase):
    def test_xmlcharrefreplace(self):
        self.assertEqual(xmlcharrefreplace(u"abc"), u"abc")
        self.assertEqual(xmlcharrefreplace(u"abc\x80"), u"abc\uFFFD")
        self.assertEqual(xmlcharrefreplace(u"abc\udc80"), u"abc\udc80")
        self.assertEqual(xmlcharrefreplace(u"abc\uffff"), u"abc\uffff")
        self.assertEqual(xmlcharrefreplace(u"abc\U00010000"), u"abc\U00010000")
        self.assertEqual(xmlcharrefreplace(u"abc\U0010ffff"), u"abc\U0010ffff")
        self.assertEqual(xmlcharrefreplace(u"abc\U00110000"), u"abc\
