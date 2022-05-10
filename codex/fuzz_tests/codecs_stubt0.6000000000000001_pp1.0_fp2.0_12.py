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

# Print a table of all codecs which can encode Unicode strings
print('%-42s%-14s%-14s%-14s%-14s%-14s%-14s' % (
    "Codec", "Unicode", "Bytes", "Escape", "XMLcharref", "BackSlash", "AddOne"))
for enc in sorted(set(codecs.aliases.values())):
    try:
        info = codecs.lookup(enc)
    except LookupError:
        continue
    print('%-42s' % enc, end=' ')
    for name in "encode", "decode":
        # Get info on each of the error handling schemes
        try:
            info.set_error(name, "strict")
            print('%-14s' % "strict", end=' ')
        except LookupError:
            print('%-14s' % "", end=' ')
        try:
            info.set_error(name, "replace")
            print('%-14s' % "replace", end=' ')
        except LookupError
