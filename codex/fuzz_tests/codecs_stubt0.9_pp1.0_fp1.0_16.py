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

class CodecXMLTextReaderTestCase(unittest.TestCase):

    def setUp(self):
        self.xml_string = """<?xml encoding="UTF-8">
<parent atr="Ala ma kota">
  <child atr="&amp;" i="1">&aacute;</child>
  <child atr="A&amp;" i="2">&oacute;&#0;</child>
  <child atr="A&amp;" i="3">&aacute;&#xaa;</child>
  <child atr="A&amp;" i="4">&#x0026;&#x00AA;</child>
  <child atr="A&amp;" i="5">&amp;</child>
  <child atr="A&amp;" i="6">&amp;</child>
  <child atr="A&amp;" i="7">&amp;</child>
  <child atr="A&amp;" i="8">&amp;</child>
  <child atr="A&
