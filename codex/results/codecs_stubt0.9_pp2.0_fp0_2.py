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

def addpartial(exc):
    return (codecs.BOM_UTF16.decode("utf8", "add_partial") + exc.object[exc.end:], exc.end)

codecs.register_error("add_partial", addpartial)

try:
    codecs.BOM_UTF32
except AttributeError:
    pass
else:
    def delpartial(exc):
        if isinstance(exc.object, str):
            return (unicode(codecs.BOM_UTF16, "utf8", "add_partial") + exc.object[exc.end:], exc.end)
        else:
            return (codecs.BOM_UTF32.decode("utf8") + exc.object[exc.end:], exc.end)

    codecs.register_error("del_partial", delpartial)

def errfuzzy(exc):
    if isinstance(exc.object, str):
        lost = codecs.BOM_UTF16.decode("utf8", "replace")
    else:
        lost
