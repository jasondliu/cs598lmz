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

for name in ('utf-8', 'utf-16', 'utf-32'):
    with codecs.open(name + '.txt', 'w', encoding=name) as f:
        f.write('ab\xe9\x87\x8d')
    with codecs.open(name + '.txt', 'r', encoding=name, errors='replace') as f:
        print('replace:', f.read())
    with codecs.open(name + '.txt', 'r', encoding=name, errors='backslashreplace') as f:
        print('backslashreplace:', f.read())
    with codecs.open(name + '.txt', 'r', encoding=name, errors='ignore') as f:
        print('ignore:', f.read())
    with codecs.open(name + '.txt', 'r', encoding=name, errors='add_one_codepoint') as f:
        print('add_one_codepoint:', f.read())
    try:
        with codecs.open(name + '.txt', 'r', encoding=name
