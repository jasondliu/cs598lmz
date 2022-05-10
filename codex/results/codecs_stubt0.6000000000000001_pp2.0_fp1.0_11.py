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

# Test all errors
for codec in [
    'ascii', 'utf-8', 'utf-16', 'utf-32',
    'iso-8859-1', 'iso-8859-15',
    'koi8_r', 'koi8_u',
    'cp037', 'cp424', 'cp437', 'cp500', 'cp737', 'cp775', 'cp850',
    'cp852', 'cp855', 'cp856', 'cp857', 'cp860', 'cp861', 'cp862',
    'cp863', 'cp864', 'cp865', 'cp866', 'cp869', 'cp874', 'cp875',
    'cp932', 'cp949', 'cp950', 'cp1006', 'cp1026', 'cp1125', 'cp1140',
    'cp1250', 'cp1251', 'cp1252', 'cp1253', 'cp1254', 'cp1255', 'cp1256',
    'cp1257', 'cp1258', 'cp65
