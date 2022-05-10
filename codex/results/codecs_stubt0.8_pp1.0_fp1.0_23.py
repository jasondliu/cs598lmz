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

c = codecs.open('utf-32-be.txt', 'rb', 'utf-32-be')
c.read(3)
c.read(3)
c.read()

c = codecs.open('utf-16-le.txt', 'rb', 'utf-16-le')
c.read(1)
c.read(1)
c.read()

c = codecs.open('utf16_be_invalid_start.txt', 'rb', 'utf-16-be')
c.read()

# Test for codecs' API
c = codecs.open('utf16_be_invalid_start.txt', 'rb', 'utf-16-be')
c.read(10)

c = codecs.open('utf16_be_invalid_start.txt', 'rb', 'utf-16-be')
c.read(3)
c.read(3)
c.read()

c = codecs.open('utf-16-be.txt', 'rb', 'utf-16-be')
c.read
