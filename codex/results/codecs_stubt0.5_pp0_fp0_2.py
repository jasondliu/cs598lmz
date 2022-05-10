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

# test decoding with "replace"
for encoding in ('ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32'):
    print(encoding, 'replace', codecs.decode('\xff', encoding, 'replace'))
print()

# test decoding with "ignore"
for encoding in ('ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32'):
    print(encoding, 'ignore', codecs.decode('\xff', encoding, 'ignore'))
print()

# test decoding with "add_one_codepoint"
for encoding in ('ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32'):
    print(encoding, 'add_one_codepoint', codecs.decode('\xff', encoding, 'add_one_codepoint'))
print()

# test decoding with "add_utf16_bytes"
for encoding in ('ascii', 'latin-1', 'utf-8
