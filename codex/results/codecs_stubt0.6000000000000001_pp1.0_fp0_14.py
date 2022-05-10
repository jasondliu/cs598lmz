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

cp1252_errorhandler = codecs.lookup_error("strict")
cp1252_decode = codecs.lookup("cp1252").decode

utf8_errorhandler = codecs.lookup_error("strict")
utf8_decode = codecs.lookup("utf-8").decode

utf8_surrogatepass_errorhandler = codecs.lookup_error("surrogatepass")
utf8_surrogatepass_decode = codecs.lookup("utf-8").decode

utf8_replace_errorhandler = codecs.lookup_error("replace")
utf8_replace_decode = codecs.lookup("utf-8").decode

utf8_ignore_errorhandler = codecs.lookup_error("ignore")
utf8_ignore_decode = codecs.lookup("utf-8").decode

utf8_xmlcharrefreplace_errorhandler = codecs.lookup_error("xmlcharrefreplace")
utf8_xmlcharrefreplace_decode = codecs.lookup("utf
