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

# Use BOM to determine byte order for both UTF-16 and UTF-32
def try_decode(fmt, data, errors="strict"):
    try:
        data.decode(fmt, errors)
    except UnicodeDecodeError as e:
        print(e)
        print(' '*e.start + '^')

print("==strict==")
try_decode("utf-8", b'\xc3\x28')
try_decode("utf-16", b'\xff\xfe\x28\x00')
try_decode("utf-16-le", b'\x28\x00')
try_decode("utf-16-be", b'\x00\x28')
try_decode("utf-32", b'\xff\xfe\x00\x00\x00\x28\x00\x00')
try_decode("utf-32-le", b'\x00\x00\x28\x00')
try_decode("utf-32-be", b'\x
