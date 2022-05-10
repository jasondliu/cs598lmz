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

print("\nTest issue 11032: utf8 fail to decode")
test_utf8_fail(b'\xe4', add_one_codepoint)
test_utf8_fail(b'\xf0\x28\x8c\x28', add_one_codepoint)
test_utf8_fail(b'\xf0\x90\x28\xbc', add_one_codepoint)

print("\nTest issue 11032: utf16 fail to decode")
test_utf16_fail(b'\x00\xe4', add_utf16_bytes)
test_utf16_fail(b'\xd8\x00\xe4\xdc', add_utf16_bytes)

print("\nTest issue 11032: utf32 fail to decode")
test_utf32_fail(b'\x00\x00\xe4\x00', add_utf32_bytes)
test_utf32_fail(b'\x00\x00\x00\xe4', add_utf32_bytes)
