import codecs
# Test codecs.register_error('xmlcharrefreplace_error', xmlcharrefreplace.xmlcharrefreplace_error)


class TestXmlcharrefreplace(unittest.TestCase):

    def test_xmlcharrefreplace(self):
        self.assertEqual(xmlcharrefreplace.xmlcharrefreplace('\u0100\u0101\u0102'), '&#256;&#257;&#258;')
        self.assertEqual(xmlcharrefreplace.xmlcharrefreplace('\u0100\u0101\u0102', False), '&#x100;&#x101;&#x102;')
        self.assertEqual(xmlcharrefreplace.xmlcharrefreplace('\u0100\u0101\u0102', True), '&#256;&#257;&#258;')
        self.assertEqual(xmlcharrefreplace.xmlcharrefreplace('\u0100\u0101\u0102', True, True), '&#x0100;&#x0101;&#x0102;')
        self.assertEqual(xmlcharrefreplace.xml
