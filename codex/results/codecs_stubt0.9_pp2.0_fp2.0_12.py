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

try:
    unicode("abc", "test.test_codecs_cn.test_encode_error")
except UnicodeEncodeError as e:
    print("error name:", e.reason)
    print("encoding:", e.encoding)
    print("start:", e.start)
    print("end:", e.end)
    print("object:", e.object)
    print("reason:", e.reason)

print("\nTesting UTF-16 encoding...")
try:
    codecs.encode("abc", "utf-16")
except UnicodeEncodeError as e:
    print("error name:", e.reason)
    print("encoding:", e.encoding)
    print("start:", e.start)
    print("end:", e.end)
    print("object:", e.object)
    print("reason:", e.reason)

print("\nTesting UTF-16BE encoding...")
try:
    codecs.encode("abc", "utf-16-be")
except UnicodeEncode
