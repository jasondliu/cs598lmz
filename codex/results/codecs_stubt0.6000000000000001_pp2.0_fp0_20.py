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

for encoding in ('utf-8', 'utf-16', 'utf-32'):
    print("Error handler:", encoding)
    for err in ('ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace',
                 'namereplace', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
        print("\tErrors:", err)
        for string in ('\x80', '\udc80', '\U00010000'):
            print("\t\tString:", string)
            for errors in ('', err, 'strict', 'surrogateescape', err+':strict', err+':surrogateescape'):
                try:
                    string.encode(encoding, errors)
                except Exception as e:
                    print("\t\t\tError:", repr(e))
                else:
                    print("\t\t\tNo error")
</code>
I am trying to understand the difference between the "strict" and "surrogateescape" error handlers when a surrogate
