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

# Issue #9591
with open("x", "w") as f:
    f.write("\U00010ffff") # U+10ffff is the highest Unicode codepoint
    f.write("\U00110000") # U+110000 is outside Unicode

try:
    with open("x", "rb") as f:
        f.read().decode("utf-8")
except UnicodeDecodeError as exc:
    print("default:", repr(exc.object[exc.start:]))
    assert exc.object[exc.start] == 0xed
    print("ignore:", repr(exc.object[exc.start:].decode("utf-8", "ignore")))

try:
    with open("x", "rb") as f:
        f.read().decode("utf-8", "replace")
except UnicodeDecodeError as exc:
    print("replace:", repr(exc.object[exc.start:].decode("utf-8", "replace")))

try:
    with open("x", "rb") as f:
        f
