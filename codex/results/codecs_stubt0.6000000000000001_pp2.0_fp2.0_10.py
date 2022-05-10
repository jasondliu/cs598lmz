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

# Test alignment errors

for encoding in ('utf-16-be', 'utf-16-le', 'utf-32-be', 'utf-32-le'):
    encoder = codecs.getencoder(encoding)
    decoder = codecs.getdecoder(encoding)

    # partial character at the end of the string
    s = encoder("\u3042")[0]
    for i in range(len(s)):
        t = s[:i]
        with self.assertRaises(UnicodeError) as cm:
            decoder(t)
        self.assertEqual(cm.exception.args[1], t)

    # partial character at the start of the string
    s = encoder("\u3042")[0]
    for i in range(len(s)):
        t = s[i:]
        with self.assertRaises(UnicodeError) as cm:
            decoder(t)
        self.assertEqual(cm.exception.args[1], t)

    # partial character at
