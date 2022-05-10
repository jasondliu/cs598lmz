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

for name in ('utf_7', 'utf_16', 'utf_16_be', 'utf_16_le',
             'utf_32', 'utf_32_be', 'utf_32_le',
             'utf7', 'utf16', 'utf32'):
    # This could be more thorough, but since we don't use those
    # codecs internally we don't care
    try:
        codecs.getincrementalencoder(name)
    except LookupError:
        continue
    print("Testing", name)
    for errors in ("strict", "replace", "ignore",
                   "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
        encoder = codecs.getincrementalencoder(name)(errors=errors)
        encoder.encode("\udc00")

print("Testing surrogateescape")
encoder = codecs.getincrementalencoder("ascii")('surrogateescape')
encoder.encode("\udc00\ud800")

print("Testing surrogatepass
