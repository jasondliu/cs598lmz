import codecs
# Test codecs.register_error("ignore", codecs.ignore_errors)
# Test codecs.register_error("replace", codecs.replace_errors)
# Test codecs.register_error("xmlcharrefreplace", codecs.xmlcharrefreplace_errors)
# Test codecs.register_error("backslashreplace", codecs.backslashreplace_errors)
# Test codecs.register_error("namereplace", codecs.namereplace_errors)

from test import test_support

# UTF-8

def test_utf8():
    assert codecs.utf_8_decode('\xc3\xa9\n') == (u'\xe9\n', 2)
    assert codecs.utf_8_decode('abcd\xc3\xa9') == (u'abcd\xe9', 5)
    assert codecs.utf_8_decode('\xc3\xa9\n', errors='ignore') == (u'\n', 2)
    assert codecs.utf_8_decode('\xc3\xa9\n', errors='replace') == (u'
