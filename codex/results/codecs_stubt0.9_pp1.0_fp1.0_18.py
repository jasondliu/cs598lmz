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

def test(encoding):
    print('-' * 33, encoding, '-' * 33)
    with codecs.open(filename, encoding=encoding, errors="ignore") as fp:
        print(fp.readline(), end='')

    with codecs.open(filename, encoding=encoding, errors="replace") as fp:
        print(fp.readline(), end='')

    with codecs.open(filename, encoding=encoding, errors='add_one_codepoint') as fp:
        print(fp.readline(), end='')

    if encoding.startswith('utf'):
        with codecs.open(filename, encoding=encoding,
                         errors='add_' + encoding + '_bytes') as fp:
            print(fp.readline(), end='')

with open(filename, 'rb') as fp:
    assert fp.read(3) == b'abc'

test('ascii')
test('utf_8')
test('utf_16')
test('utf_32')
