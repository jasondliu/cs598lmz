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
#    exception handling
#
def eofdecode(exc):
    print("EOF already reached:", exc.object)
    return u"", exc.end

codecs.register_error("eof_decode", eofdecode)
decoder = codecs.getdecoder("latin-1")
decoder("abc", "eof_decode")

print("testing unknown handler ...")
def unknown_handler(exc):
    print("CHEATER:", exc)
    return (u"CHEATER", 1)

codecs.register_error("unknown_handler", unknown_handler)

import unicodedata # need unaccented characters
try:
    unicodedata.normalize("NFKD", "cheater") # raises exception!
except Exception as exc:
    unicode(exc)
    unicodedata.normalize("NFKD", "cheater", "unknown_handler")

#
#    buffer errors
#
def badbytes(exc):
    return (u"\ufffd", exc.end) # replacement
