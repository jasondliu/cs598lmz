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
#
# Test encode error handlers
def check_unicode_encode_error_handler(encoding, input, expected, errors):
    for errorhandler in (None, "strict", "replace", "xmlcharrefreplace",
                         "ignore", "backslashreplace"):
        if errorhandler == "strict":
            exc_type = UnicodeEncodeError
            if encoding in ("utf7", "utf8"):
                exc_type = ValueError
        elif errorhandler == "replace":
            exc_type = None
        elif errorhandler == "xmlcharrefreplace":
            exc_type = None
        elif errorhandler == "ignore":
            exc_type = None
        elif errorhandler == "backslashreplace":
            exc_type = None
        elif errorhandler is None:
            exc_type = UnicodeEncodeError
        else:
            print("unknown errorhandler", errorhandler)
            continue
        try:
            codecs.encode(input, encoding, errorhandler)
        except exc_type as detail:
            if exc_type is UnicodeEn
