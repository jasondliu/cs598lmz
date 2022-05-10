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

buf = "řab".encode("utf-8")

try:
    buf.decode("utf-8")
except UnicodeDecodeError as e:
    print("{!s} at position {}: {}".format(e, e.start, str(e)))
    print(e.object[e.start:e.end])

try:
    buf.decode("utf-8", "add_one_codepoint")
except UnicodeDecodeError as e:
    print("{!s} at position {}: {}".format(e, e.start, str(e)))
    print(e.object[e.start:e.end])

try:
    buf.decode("utf-8", "replace")
except UnicodeDecodeError as e:
    print("{!s} at position {}: {}".format(e, e.start, str(e)))
    print(e.object[e.start:e.end])

try:
    buf.decode("iso8859-2")
except UnicodeDecodeError as e:
    print
