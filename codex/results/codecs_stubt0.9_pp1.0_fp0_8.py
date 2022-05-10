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

def basic_nul():
    buf = b'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(buf)):
        exp_buf = [buf[0:i], buf[i:]]
        with codecs.open('nul', 'rb', 'utf-16', errors='strict') as f:
            text = f.read()
            assert text == u'', "error in nul codec"
        with codecs.open('nul', 'wb', 'utf-16', errors='strict') as f:
            f.write(u'abcdefg')
        with codecs.open('nul', 'rb', 'utf-16', errors='strict') as f:
            text = f.read()
            assert text == u'', "error in nul codec"
        with codecs.open('nul', 'wb', 'utf-32', errors='strict') as f:
            f.write(u'abcdefg')
        with codecs.open('nul', 'rb', 'utf-32
