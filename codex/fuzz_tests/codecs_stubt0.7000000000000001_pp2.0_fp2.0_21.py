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

print(codecs.decode(b'\x00\x00\x00\x00', "utf-32", "add_one_codepoint"))
print(codecs.decode(b'\x00\x00\x00\x00', "utf-32", "add_utf32_bytes"))
print(codecs.decode(b'\x00\x00\x00\x00', "utf-16", "add_one_codepoint"))
print(codecs.decode(b'\x00\x00\x00\x00', "utf-16", "add_utf16_bytes"))
</code>

<code>&gt;&gt;&gt; python3 test.py
Traceback (most recent call last):
  File "test.py", line 13, in &lt;module&gt;
    print(codecs.decode(b'\x00\x00\x00\x00', "utf-32", "add_one_codepoint"))
  File "/Users/bods
