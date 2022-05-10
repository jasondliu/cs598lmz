import codecs
# Test codecs.register_error

import codecs

def bad_errorhandler(exception):
    return u"\ufffd", exception.end

codecs.register_error("bad", bad_errorhandler)

def test():
    assert codecs.strict_errors == "strict"
    assert codecs.ignore_errors == "ignore"
    assert codecs.replace_errors == "replace"
    assert codecs.xmlcharrefreplace_errors == "xmlcharrefreplace"
    assert codecs.backslashreplace_errors == "backslashreplace"

    assert codecs.lookup_error("strict") == codecs.strict_errors
    assert codecs.lookup_error("ignore") == codecs.ignore_errors
    assert codecs.lookup_error("replace") == codecs.replace_errors
    assert codecs.lookup_error("xmlcharrefreplace") == codecs.xmlcharrefreplace_errors
    assert codecs.lookup_error("backslashreplace") == codecs.backslashreplace_errors
    assert codecs.lookup_error("bad
