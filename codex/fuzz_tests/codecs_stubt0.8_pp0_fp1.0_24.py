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

a_cp1251_bom = codecs.lookup('cp1251').encode(u"a")[0]

bom_codecs = {
    codecs.BOM_UTF32_BE : [('utf32-be', 'big'), 
                           ('utf32-le', 'little'),
                           ('utf-16-be', 'utf-16-be'),
                           ('utf-16-le', 'utf-16-le'),
                           ('utf-8', 'utf-8')],
    codecs.BOM_UTF32_LE : [('utf32-be', 'little'), 
                           ('utf32-le', 'big'),
                           ('utf-16-be', 'utf-16-le'),
                           ('utf-16-le', 'utf-16-be'),
                           ('utf-8', 'utf-8')],
    codecs.BOM_UTF16_BE : [('utf16-be', 'utf-16-be'), 
                           ('utf16-le', 'utf-16-le'),
                
