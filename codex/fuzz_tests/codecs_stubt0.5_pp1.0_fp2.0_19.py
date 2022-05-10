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

u = chr(0xD800)

for encoding in "utf-16", "utf-16-be", "utf-16-le", "utf-32", "utf-32-be", "utf-32-le":
    for errors in "strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes":
        print(encoding, errors)
        try:
            print(u.encode(encoding, errors))
        except UnicodeEncodeError as e:
            print(e)
        try:
            print(u.encode(encoding, errors).decode(encoding, errors))
        except UnicodeDecodeError as e:
            print(e)
</code>
output
<code>utf-16 strict
Traceback (most recent call last):
  File "test.py", line 23, in &lt;module&gt;
    print(u.encode(encoding, errors))
UnicodeEncodeError: 'utf-16-be' codec can't
