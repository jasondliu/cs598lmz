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

add_one_codepoint_exc = codecs.lookup_error("add_one_codepoint")
add_utf16_bytes_exc = codecs.lookup_error("add_utf16_bytes")
add_utf32_bytes_exc = codecs.lookup_error("add_utf32_bytes")

errors = ['strict', 'ignore', 'replace', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes']

# UTF-8
encoding = 'utf-8'
name = 'utf-8'

for errors_var in errors:
    print errors_var
    for byte in xrange(0, 0x100):
        byte = chr(byte)
        print '%02x' % ord(byte),
        try:
            unicode(byte, encoding, errors_var)
        except UnicodeDecodeError, exc:
            print
        except ValueError:
            print 'ValueError'
        except UnicodeEncodeError, exc: # Encode to UTF8
            print 'Un
