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

encoding_map = {
    'utf-8' : 'utf-8-sig',
    'utf-16' : 'utf-16-le',
    'utf-32' : 'utf-32-le'
}

def read_file(filename, encoding):
    with codecs.open(filename, 'r', encoding=encoding_map[encoding], errors='add_one_codepoint') as f:
        return f.read()

def write_file(filename, content, encoding):
    with codecs.open(filename, 'w', encoding=encoding_map[encoding], errors='add_one_codepoint') as f:
        f.write(content)

def write_file_utf16(filename, content):
    with codecs.open(filename, 'w', encoding='utf-16-le', errors='add_utf16_bytes') as f:
        f.write(content)

def write_file_utf32(filename, content):
    with codecs.open(filename, 'w', encoding='utf-32-
