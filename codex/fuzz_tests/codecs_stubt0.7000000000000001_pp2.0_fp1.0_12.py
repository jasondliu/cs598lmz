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

# test decoding
encodings = ('utf-16', 'utf-16-le', 'utf-16-be', 'utf-32', 'utf-32-le', 'utf-32-be')
for encoding in encodings:
    print('-'*20, encoding, '-'*20)
    for i in range(4):
        print('i=', i)
        v = b'ab' + b'\0'*i
        print('v=',v)
        try:
            u = v.decode(encoding)
        except UnicodeDecodeError as exc:
            print('UnicodeDecodeError', exc)
            u = v.decode(encoding, 'add_one_codepoint')
            print('v.decode(encoding, add_one_codepoint)=', repr(u))
            u = v.decode(encoding, 'add_utf16_bytes')
            print('v.decode(encoding, add_utf16_bytes)=', repr(u))
            u = v.decode(encoding,
