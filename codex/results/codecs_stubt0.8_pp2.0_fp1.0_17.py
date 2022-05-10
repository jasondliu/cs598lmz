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

def run_encode_error(name, codec, enc, err, src):
    dest = "%s_encodeerror_%d_%%s.txt" % (name, err)
    writer = codecs.getwriter(enc)
    for s in src, b'abcd':
        with open(dest % s, 'wb') as f:
            f.write(b'# source: ')
            f.write(s)
            f.write(b'\n')
            f.write(b'# encoding: ')
            f.write(enc.encode('ascii'))
            f.write(b'\n')
            f.write(b'# error handling: ')
            f.write(err.encode('ascii'))
            f.write(b'\n')
            f.write(b'#\n')
            f.flush()

            fc = writer(f, encoding=enc, errors=err)
            fc.write(s)
            fc.write('a')
            fc.
