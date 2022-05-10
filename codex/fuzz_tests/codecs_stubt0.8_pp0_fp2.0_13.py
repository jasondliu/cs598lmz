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

txt = "caf\xe9"

for encoding in ["utf-8", "utf-8-variants", "utf-16", "utf-32"]:
    try:
        print(txt.encode(encoding, "add_one_codepoint"))
    except UnicodeEncodeError:
        print("failed to encode in {}".format(encoding))
    try:
        print(txt.encode(encoding, "add_utf16_bytes"))
    except UnicodeEncodeError:
        print("failed to encode in {}".format(encoding))
    try:
        print(txt.encode(encoding, "add_utf32_bytes"))
    except UnicodeEncodeError:
        print("failed to encode in {}".format(encoding))
</code>
The output is, as expected,
<code>caf�
failed to encode in utf-8
failed to encode in utf-8
caf�
failed to encode in utf-8-variants
failed to encode in utf-8-variants
failed to encode in utf-
