import codecs
# Test codecs.register_error
import encodings.utf_8

def test_main():
    # Test codecs.register_error
    def my_handler(exception):
        return ("", exception.end)
    codecs.register_error("my_handler", my_handler)
    assert codecs.lookup_error("my_handler") is my_handler
    assert encodings.utf_8.lookup_error("my_handler") is my_handler
    # Test codecs.lookup_error
    assert codecs.lookup_error("strict") is codecs.strict_errors
    assert codecs.lookup_error("ignore") is codecs.ignore_errors
    assert codecs.lookup_error("replace") is codecs.replace_errors
    assert codecs.lookup_error("xmlcharrefreplace") is codecs.xmlcharrefreplace_errors
    assert codecs.lookup_error("backslashreplace") is codecs.backslashreplace_errors
    assert codecs.lookup_error("namereplace") is codecs.namereplace_errors
    #
