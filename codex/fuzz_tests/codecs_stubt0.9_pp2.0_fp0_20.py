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

if __name__ == "__main__":
    # First, test a 1-to-1 encoding
    msg = 'Spicy Jalapen\u0303o'
    for errors in ('strict', 'replace', 'ignore', 'surrogateescape', 'surrogatepass',
                   'backslashreplace', 'xmlcharrefreplace'):
        print('%s: %s' % (errors, msg.encode('ascii', errors)))
    es = 'add_one_codepoint'
    ws = 'add_utf16_bytes'
    xs = 'add_utf32_bytes'
    for errors in (es, ws, xs):
        print('%s: %s' % (errors, msg.encode('ascii', errors)))

    # Now, test an encoding where the output of the error handler includes
    # the same byte value as the replacement character
    msg = 'Spicy Jalap\u0303\u0303n\u0303o'
    for errors in ('strict', 'replace', 'ignore', 'surrog
