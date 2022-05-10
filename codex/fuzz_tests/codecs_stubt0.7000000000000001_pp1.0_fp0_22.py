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

bugle = open('bugle.txt', 'rb').read()

# test all codecs with different error handlers
for codec in ('utf-8', 'utf-16', 'utf-32'):
    print('{} (with add_one_codepoint)'.format(codec))
    print(bugle.decode(codec, 'add_one_codepoint'))
    print('{} (with add_utf16_bytes)'.format(codec))
    print(bugle.decode(codec, 'add_utf16_bytes'))
    print('{} (with add_utf32_bytes)'.format(codec))
    print(bugle.decode(codec, 'add_utf32_bytes'))
</code>
Output:
<code>utf-8 (with add_one_codepoint)
aનવરાત્રિ
utf-8 (with add_utf16_bytes)
aનવર
