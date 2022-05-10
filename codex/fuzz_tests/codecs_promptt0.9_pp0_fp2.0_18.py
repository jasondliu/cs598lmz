import codecs
# Test codecs.register_error with


from codecs import BOM
from test.test_support import check_warnings

def test_decode_charref():
    def charref(text):
        return codecs.getdecoder("xmlcharrefreplace")(text)[0]

    check_error_handling("decoding xml character references", "xmlcharref", charref, {
        "a":           u("a"),
        "&#97;":       u("a"),
        "&#x61;":      u("a"),
        "&#0141;":     u("&#0141;"),
        "&#x&#x61;":   u("&#x&#x61;"),
        "&#x2e;":      u("&#x2e;"),
        "&#xFFFFFFFF;":u("\U0010ffff"),
        }
        )
    assert charref("&#9999999999;") == u("&#9999999999;")

def test_register_error():
    def charref(text):
        return codecs.getdecoder
