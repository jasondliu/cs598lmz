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

def test(str_, encoding, error):
    data = bytes(str_, encoding)
    print(repr(data))
    print(repr(''.join(chr(x) for x in data)))
    try:
        print(repr(data.decode(encoding)))
    except UnicodeDecodeError as e:
        print(e)
        print(repr(data.decode(encoding, errors=error)))
    # repr(x.encode(encoding, errors=error)) is equal to repr(x)


print('cp1252')
test('ab\u0304bc\xad', 'cp1252', 'replace')
print()

print('iso-8859-15')
test('ab\u0304bc', 'iso-8859-15', 'replace')
print()

print('utf-8')
test('ab\ufeffbc', 'utf-8', 'replace')
test('ab\ufffebc', 'utf-8', 'replace')
test('ab\u0304bc', 'utf-8',
